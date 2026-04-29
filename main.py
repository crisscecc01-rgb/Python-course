import PokemonStory
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib
import os

if __name__ == "__main__":
    model = None
    feature_names = None
    number_cycles = 1000
    story = []
    end_story = None
    print("Want to randomize? (y/n)")
    choice = input("> ").strip().lower()
    while choice != "y" and choice != "n":
        print("please select y or n")
        choice = input("> ").strip().lower()

    if choice == "n":
        i=1
        model_path = "pokemon_rf_model.pkl"
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                feature_names = joblib.load("pokemon_rf_features.pkl")
                print("ML model loaded!")
            except Exception as e:
                print("Error during the loading of the ML model: ", e)
        else:
            print("WARNING: ML model not found!")
            print("Run the randomization to generate the model first:", model, feature_names)
            model = None
        PokemonStory.BeginStory("1", story, choice, model, feature_names)
    elif choice == "y":
        for i in range(number_cycles):
            print(f"{i}")
            PokemonStory.BeginStory("1", story, choice, None, None)

        records = []

        for game_idx, sim in enumerate(story):
            num_battles = len(sim["wild_pokemons"])

            for i in range(num_battles):
                for t in range(sim["total_num_turns"][i]):
                    records.append({
                        "Starter": sim["my_pokemons"][i],
                        "Starter_Types": sim["my_pokemon_type"][i],
                        "Starter_Level": sim["my_level"][i],
                        "Starter_Stats": sim["my_pokemon_stats"][i],
                        "Game": game_idx + 1,
                        "Battle_Number": i + 1,
                        "Enemy_Pokemon": sim["wild_pokemons"][i],
                        "Enemy_Pokemon_Types": sim["wild_pokemon_type"][i],
                        "Enemy_Pokemon_Level": sim["wild_pokemon_level"][i],
                        "Enemy_Pokemon_Stats" : sim["wild_pokemon_stats"][i],
                        "Win": sim["win_loss"][i],
                        "Win_Percentage": sim["win_loss"][i]*100,
                        "Left_HP": sim["left_hp"][i],
                        "Turns": sim["total_num_turns"][i],
                        "Actual_turn": t+1,
                        "pk_HP": sim["battle_turn_details"][i]["my_pk"][t]["pk_hp"],
                        "pk_Move": sim["battle_turn_details"][i]["my_pk"][t]["pk_move"],
                        "pk_Damage": sim["battle_turn_details"][i]["my_pk"][t]["pk_damage"],
                        "Enemy_HP": sim["battle_turn_details"][i]["enemy_pk"][t]["pk_hp"],
                        "Enemy_Move": sim["battle_turn_details"][i]["enemy_pk"][t]["pk_move"],
                        "Enemy_Damage": sim["battle_turn_details"][i]["enemy_pk"][t]["pk_damage"],
                    })
        df_master_complete = pd.DataFrame(records)
        # ============================
        # 1. Stats explosion
        # ============================
        my_stats_df = pd.json_normalize(df_master_complete["Starter_Stats"]).add_prefix("Starter_Stat_")
        enemy_stats_df = pd.json_normalize(df_master_complete["Enemy_Pokemon_Stats"]).add_prefix("Enemy_Stat_")

        df_master_complete = df_master_complete.join(my_stats_df)
        df_master_complete = df_master_complete.join(enemy_stats_df)

        df_master_complete = df_master_complete.drop(columns=["Starter_Stats", "Enemy_Pokemon_Stats"])
        # ============================
        # 2. Types explosion
        # ============================
        # Starter types
        df_master_complete["Starter_Type_1"] = df_master_complete["Starter_Types"].apply(
            lambda t: t[0] if len(t) > 0 else None)
        df_master_complete["Starter_Type_2"] = df_master_complete["Starter_Types"].apply(
            lambda t: t[1] if len(t) > 1 else None)
        # Wild types
        df_master_complete["Enemy_Type_1"] = df_master_complete["Enemy_Pokemon_Types"].apply(
            lambda t: t[0] if len(t) > 0 else None)
        df_master_complete["Enemy_Type_2"] = df_master_complete["Enemy_Pokemon_Types"].apply(
            lambda t: t[1] if len(t) > 1 else None)
        # ============================
        # 3. Column reorder
        # ============================
        first_cols = ["Starter", "Starter_Level", "Game"]

        starter_type_cols = ["Starter_Type_1", "Starter_Type_2"]
        starter_stat_cols = [c for c in df_master_complete.columns if c.startswith("Starter_Stat_")]

        enemy_type_cols = ["Enemy_Type_1", "Enemy_Type_2"]
        enemy_stat_cols = [c for c in df_master_complete.columns if c.startswith("Enemy_Stat_")]

        # All the other columns
        other_cols = [
            c for c in df_master_complete.columns
            if c not in first_cols + starter_type_cols + starter_stat_cols + enemy_type_cols + enemy_stat_cols
        ]
        # Final order
        df_master_complete = df_master_complete[
            first_cols +
            starter_type_cols +
            starter_stat_cols +
            enemy_type_cols +
            enemy_stat_cols +
            other_cols
            ]
        print(df_master_complete)
        # ============================
        # 1. Copy of the dataset
        # ============================
        df_battles = df_master_complete.drop_duplicates(
            subset=["Game", "Battle_Number"]
        ).reset_index(drop=True)
        df_ml = df_battles.copy()
        # Columns to be dropped
        cols_to_drop = [
            "Starter",
            "Starter_Types",
            "Enemy_Pokemon",
            "Enemy_Pokemon_Types",
            "pk_Move",
            "Enemy_Move",
            "Battle_Number",
            "Win_Percentage",
            "Turns",
            "Actual_turn",
            "Starter_Stat_hp",
            "pk_Damage",
            "Enemy_HP",
            "Enemy_Damage",
            "Left_HP",
            "Game"
        ]
        df_ml = df_ml.drop(columns=cols_to_drop)
        # ============================
        # 2. ONE-HOT ENCODING For pk types
        # ============================

        first_cols = ["Starter_Level", "pk_HP"]
        other_cols = [
            c for c in df_ml.columns
            if c not in first_cols
        ]

        df_ml = df_ml[first_cols+other_cols]

        type_cols = [
            "Starter_Type_1", "Starter_Type_2",
            "Enemy_Type_1", "Enemy_Type_2"
        ]
        df_ml = pd.get_dummies(df_ml, columns=type_cols)
        print(df_ml)
        # ============================
        # 3. Features and target definition
        # ============================
        y = df_ml["Win"]
        X = df_ml.drop(columns=["Win"])
        # ============================
        # 4. TRAIN/TEST SPLIT
        # ============================
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )
        # ============================
        # 5. RANDOM FOREST
        # ============================
        model = RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42
        )
        model.fit(X_train, y_train)
        # ============================
        # 6. Evaluation
        # ============================
        pred = model.predict(X_test)
        probs = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, pred)
        auc = roc_auc_score(y_test, probs)

        print("Accuracy:", acc)
        print("ROC AUC:", auc)

        joblib.dump(model, "pokemon_rf_model.pkl")
        feature_names = list(X.columns)
        joblib.dump(feature_names, "pokemon_rf_features.pkl")

        print("Model saved!")








