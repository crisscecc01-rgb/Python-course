import PokemonStory
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
import Database as Db
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.colors as mcolors

if __name__ == "__main__":
    number_cycles = 451
    story = {"Bulbasaur": [],
             "Charmander": [],
             "Squirtle": []}
    end_story = None
    print("Want to randomize? (y/n)")
    choice = input("> ").strip().lower()
    while choice != "y" and choice != "n":
        print("please select y or n")
        choice = input("> ").strip().lower()


    if choice == "n":
        i=1
        PokemonStory.BeginStory("1", story, choice)
    elif choice == "y":
        for i in range(number_cycles):
            print(f"{i}")
            if i < round((number_cycles-1)/3)*1:
                PokemonStory.BeginStory(list(story.keys())[0],story,choice)
            elif i < round((number_cycles - 1) / 3)*2:
                PokemonStory.BeginStory(list(story.keys())[1],story,choice)
            elif i < round((number_cycles - 1) / 3)*3:
                PokemonStory.BeginStory(list(story.keys())[2],story,choice)

        records = []
        for starter, simulations in story.items():
            for game_idx, sim in enumerate(simulations):
                num_battles = len(sim["wild_pokemons"])

                for i in range(num_battles):
                    for t in range(sim["total_num_turns"][i]):
                        records.append({
                            "Starter": starter,
                            "Starter_Level": sim["my_level"][i],
                            "Game": game_idx + 1,
                            "Battle_Number": i + 1,
                            "Enemy_Pokemon": sim["wild_pokemons"][i],
                            "Enemy_Pokemon_Types": sim["wild_pokemon_type"][i],
                            "Enemy_Pokemon_Level": sim["wild_pokemon_level"][i],
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
        #print(df_master_complete)
        df_master_battles = df_master_complete.drop_duplicates(subset=["Starter", "Game", "Battle_Number"])



        sns.set_theme()
        colors_starter = {"Bulbasaur": "green", "Charmander": "red", "Squirtle": "blue"}

        # =========================================================
        # SIMPLE PLOT
        # =========================================================
        df_master_complete['max_hp_battle'] = df_master_complete.groupby(['Starter', 'Game', 'Battle_Number'])['pk_HP'].transform('first')
        df_master_complete['pk_HP_perc'] = (df_master_complete['pk_HP'] / df_master_complete['max_hp_battle']) * 100
        df_master_complete['next_pk_HP_perc'] = df_master_complete.groupby(['Starter', 'Game', 'Battle_Number'])['pk_HP_perc'].shift(-1)
        df_master_complete['HP_reduction'] = df_master_complete['pk_HP_perc'] - df_master_complete['next_pk_HP_perc']
        df_master_complete.loc[(df_master_complete['next_pk_HP_perc'].isna()) & (df_master_complete['Win'] == 1), 'HP_reduction'] = 0
        df_master_complete.loc[(df_master_complete['next_pk_HP_perc'].isna()) & (df_master_complete['Win'] == 0), 'HP_reduction'] = df_master_complete['pk_HP_perc']

        #print(df_master_complete)
        plt.figure(1, figsize=(10, 5))
        sns.lineplot(data=df_master_complete, x="Actual_turn", y="HP_reduction", hue="Starter",
                     palette=colors_starter,errorbar='sd', marker='o', linewidth=2)
        plt.title("Percentage Reduction of trainer Pokémon HP per Starter", fontsize=14, fontweight='bold')
        plt.xlabel("Number of Turns", fontsize=12)
        plt.ylabel("Percentage Reduction of HP", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        # =========================================================
        # PIE PLOT
        # =========================================================
        df_master_moves = df_master_complete[df_master_complete['pk_Move'].str.strip()!= ""]
        move_usage = df_master_moves.groupby(['Starter'])['pk_Move'].value_counts().reset_index()
        damage_df = df_master_moves.groupby(['Starter','pk_Move'])['pk_Damage'].sum().reset_index()
        move_usage = pd.merge(move_usage, damage_df, on=['Starter','pk_Move'], how='right')
        #print(move_usage)

        fig1, axes = plt.subplots(2, 3, figsize=(15, 6))
        index_starter = df_master_complete['Starter'].unique()

        for col, pokemon in enumerate(index_starter):
            df_filtered = move_usage[move_usage['Starter'] == pokemon]

            ax_usage = axes[0, col]
            ax_usage.pie(df_filtered['count'], labels=df_filtered['pk_Move'], autopct='%1.1f%%', startangle=90)
            ax_usage.set_title(f"{pokemon} - Usage", fontsize=14, fontweight='bold')

            ax_damage = axes[1, col]
            ax_damage.pie(df_filtered['pk_Damage'], labels=df_filtered['pk_Move'], autopct='%1.1f%%', startangle=90)
            ax_damage.set_title(f"{pokemon} - Damage", fontsize=14, fontweight='bold')

        plt.tight_layout()

        df_master_types_exploded = df_master_complete['Enemy_Pokemon_Types'].explode().reset_index()
        enemy_types_found = df_master_types_exploded['Enemy_Pokemon_Types'].value_counts().reset_index()

        database_types_exploded = Db.P_db.Pokemon_df['types'].explode().reset_index()
        database_types = database_types_exploded['types'].value_counts().reset_index()


        #print(database_types)
        #print(enemy_types_found)

        fig2, axes = plt.subplots(1, 2, figsize=(15, 6))
        ax_usage = axes[0]
        ax_usage.pie(database_types['count'], labels=database_types['types'], autopct='%1.1f%%', startangle=90)
        ax_usage.set_title(f"Database Pokemon types", fontsize=14, fontweight='bold')
        ax_usage = axes[1]
        ax_usage.pie(enemy_types_found['count'], labels=enemy_types_found['Enemy_Pokemon_Types'], autopct='%1.1f%%', startangle=90)
        ax_usage.set_title(f"Enemy Pokemon Types found", fontsize=14, fontweight='bold')
        plt.tight_layout()

        #========================================================

        fig3, axes = plt.subplots(1, 2, figsize=(15, 6))
        sns.barplot(data = database_types, x= 'types', y= 'count', ax=axes[0], hue= 'types',legend=False)
        axes[0].set_title(f"Database Pokemon types", fontsize=14, fontweight='bold')
        axes[0].tick_params(axis='x',rotation=90)
        sns.barplot(data=enemy_types_found, x='Enemy_Pokemon_Types', y='count', ax=axes[1], hue='Enemy_Pokemon_Types')
        axes[1].set_title(f"Enemy Pokemon Types found", fontsize=14, fontweight='bold')
        axes[1].tick_params(axis='x',rotation=90)
        plt.tight_layout()

        # =========================================================
        # BAR PLOT
        # =========================================================
        master_damage_filtered = df_master_complete[df_master_complete['pk_Move'].str.strip()!=""]
        #print(master_damage_filtered)
        pk_damage_lvl_dist = master_damage_filtered.groupby(['Starter','Starter_Level'])['pk_Damage'].mean().reset_index()
        #print(pk_damage_lvl_dist)

        fig4, axes = plt.subplots(1, 3, figsize=(15, 6))
        index_starter = df_master_complete['Starter'].unique()

        for col, pokemon in enumerate(index_starter):
            df_filtered = pk_damage_lvl_dist[pk_damage_lvl_dist['Starter'] == pokemon]
            sns.barplot(data=df_filtered, x='Starter_Level', y='pk_Damage', ax=axes[col], hue='Starter', palette=colors_starter, legend=False)
            axes[col].set_title(f"Average Damage done by {index_starter[col]}", fontsize=14, fontweight='bold')
            axes[col].tick_params(axis='x', rotation=90)
            axes[col].set_xlabel(f"{index_starter[col]} level")
            if col == 0:
                axes[col].set_ylabel("Pk Damage")
            else:
                axes[col].set_ylabel("")

        plt.tight_layout()

        # =========================================================
        # IMAGE PLOT
        # =========================================================
        df_master_complete = df_master_complete.explode('Enemy_Pokemon_Types')
        df_master_complete = df_master_complete.reset_index(drop=True)
        #print(df_master_complete)
        image_3d_plot_df = df_master_complete[['Starter','Win','Enemy_Pokemon_Level','Enemy_Pokemon_Types']]
        image_3d_plot_df_mean = df_master_complete.groupby(['Starter', 'Enemy_Pokemon_Level','Enemy_Pokemon_Types'])['Win'].mean().reset_index()
        #print(image_3d_plot_df_mean)
        found_types = sorted(image_3d_plot_df_mean['Enemy_Pokemon_Types'].unique())
        type_to_num = {tipo: i for i, tipo in enumerate(found_types)}
        cmaps = {
            'Bulbasaur': mcolors.LinearSegmentedColormap.from_list("BulbaG", ["#f0f0f0", "forestgreen"]),
            'Charmander': mcolors.LinearSegmentedColormap.from_list("CharG", ["#f0f0f0", "crimson"]),
            'Squirtle': mcolors.LinearSegmentedColormap.from_list("SquirG", ["#f0f0f0", "royalblue"])
        }

        fig5 = plt.figure(figsize=(18, 6))

        for col, pokemon in enumerate(index_starter):
            df_filtered = image_3d_plot_df_mean[image_3d_plot_df_mean['Starter'] == pokemon]

            ax = fig5.add_subplot(1, 3, col + 1, projection='3d')

            x = df_filtered['Enemy_Pokemon_Level'].values
            y = df_filtered['Enemy_Pokemon_Types'].map(type_to_num).values
            z = np.zeros(len(df_filtered))

            dx = 0.5
            dy = 0.5
            dz = df_filtered['Win'].values

            current_cmap = cmaps.get(pokemon, plt.get_cmap('viridis'))
            bar_colors = current_cmap(dz)
            for i in range(len(bar_colors)):
                bar_colors[i, 3] = 0.3 + (dz[i] * 0.6)

            ax.bar3d(x - dx / 2, y - dy / 2, z, dx, dy, dz, color=bar_colors, alpha=0.7, edgecolors='black',
                     linewidth=0.2)

            ax.set_title(f"Win Rate: {pokemon}", fontsize=15, fontweight='bold', pad=20)
            ax.set_xlabel('Enemy Level', fontsize=10, labelpad=10)
            ax.set_ylabel('Enemy Type', fontsize=10, labelpad=15)
            ax.set_zlabel('Win %', fontsize=10, labelpad=10)



            levels = sorted(image_3d_plot_df_mean['Enemy_Pokemon_Level'].unique())
            ax.set_xticks(levels)

            ax.set_xticklabels(levels, fontsize=8, ha='center', va='center')
            ax.tick_params(axis='x', pad=5)


            ax.set_yticks(range(len(found_types)))

            ax.set_yticklabels(found_types, fontsize=8, rotation=-15, ha='center', va='center')
            ax.tick_params(axis='y', pad=8)

            ax.set_zlim(0, 1)
            ax.view_init(elev=35, azim=-20)

        plt.suptitle("3D Analysis: Win Rate by Level and Enemy Type", fontsize=20, fontweight='bold', y=0.98)




        plt.show()







