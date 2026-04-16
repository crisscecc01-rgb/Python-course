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
    number_cycles = 151
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
        print(df_master_complete)
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
        print(pk_damage_lvl_dist)

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
        print(df_master_complete)
        image_3d_plot_df = df_master_complete[['Starter','Win','Enemy_Pokemon_Level','Enemy_Pokemon_Types']]
        image_3d_plot_df_mean = df_master_complete.groupby(['Starter', 'Enemy_Pokemon_Level','Enemy_Pokemon_Types'])['Win'].mean().reset_index()
        print(image_3d_plot_df_mean)
        found_types = sorted(image_3d_plot_df_mean['Enemy_Pokemon_Types'].unique())
        type_to_num = {tipo: i for i, tipo in enumerate(found_types)}
        cmaps = {
            'Bulbasaur': mcolors.LinearSegmentedColormap.from_list("BulbaG", ["#f0f0f0", "forestgreen"]),
            'Charmander': mcolors.LinearSegmentedColormap.from_list("CharG", ["#f0f0f0", "crimson"]),
            'Squirtle': mcolors.LinearSegmentedColormap.from_list("SquirG", ["#f0f0f0", "royalblue"])
        }

        fig5, ax = plt.subplots(1,3,figsize=(15, 6))
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
                bar_colors[i, 3] = 0.3 + (dz[i] * 0.6)  # Parte da 0.3 e arriva a 0.9

            ax.bar3d(x, y, z, dx, dy, dz, color = bar_colors, alpha=0.7, edgecolors='black', linewidth=0.2)

            ax.set_title(f"Win Rate: {pokemon}", fontsize=15, fontweight='bold', pad=20)
            ax.set_xlabel('Enemy Level', fontsize=10)
            ax.set_ylabel('Enemy Type', fontsize=10)
            ax.set_zlabel('Win %', fontsize=10)

            ax.set_yticks(range(len(found_types)))
            ax.set_yticklabels(found_types, fontsize=7, rotation=-15, ha='right')
            ax.set_zlim(0, 1)
            ax.view_init(elev=25, azim=-50)
        plt.suptitle("3D Analysis: Win Rate by Level and Enemy Type", fontsize=20, fontweight='bold', y=0.95)
        plt.show()

        '''
        # =========================================================
        # SIMPLE PLOT
        # =========================================================
    
        plt.figure(20, figsize=(10, 5))
        cumulative_wins = df_master_battles.groupby(['Starter', 'Battle_Number'])['Win'].mean().groupby(
            'Starter').cumsum().reset_index()
        sns.lineplot(data=cumulative_wins, x="Battle_Number", y="Win", hue="Starter",
                     palette=colors_starter, marker='o', linewidth=2)
        plt.title("Cumulative Average Victories per Starter", fontsize=14, fontweight='bold')
        plt.xlabel("Number of Battles", fontsize=12)
        plt.ylabel("Average Cumulative Victories", fontsize=12)
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        # =========================================================
        # BOXPLOT
        # =========================================================
        fig10, axes = plt.subplots(1, 2, figsize=(15, 6))

        sns.boxplot(data=df_master_battles, x="Starter", y="Turns", hue="Starter", palette=colors_starter, ax=axes[0])
        axes[0].set_title("Battle Lengths (Number of Turns)", fontweight='bold')

        df_master_battles_described_turns = df_master_battles.groupby('Starter')['Turns'].describe()

        index_starter = df_master_battles_described_turns.index

        testo = ""
        for starter in index_starter:
            testo += (
                f"{starter} : Mean: {df_master_battles_described_turns.loc[starter, 'mean']:.2f} | Median: {df_master_battles_described_turns.loc[starter, '50%']:.2f} | 25%:"
                f" {df_master_battles_described_turns.loc[starter, '25%']:.2f} | 75%: {df_master_battles_described_turns.loc[starter, '75%']:.2f}\n")
        axes[0].text(0.95, 0.95, testo, transform=axes[0].transAxes, fontsize=10,
                 verticalalignment='top', horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        sns.boxplot(data=df_master_battles, x="Starter", y="Left_HP", hue="Starter", palette=colors_starter, ax=axes[1])
        axes[1].set_title("Remaining HP at End of Battle", fontweight='bold')

        df_master_battles_described_hp = df_master_battles.groupby('Starter')['Left_HP'].describe()
        testo = ""
        for starter in index_starter:
            testo += (
                f"{starter} : Mean: {df_master_battles_described_hp.loc[starter, 'mean']:.2f} | Median: {df_master_battles_described_hp.loc[starter, '50%']:.2f} | 25%:"
                f" {df_master_battles_described_hp.loc[starter, '25%']:.2f} | 75%: {df_master_battles_described_hp.loc[starter, '75%']:.2f}\n")
        axes[1].text(0.95, 0.95, testo, transform=axes[1].transAxes, fontsize=10,
                 verticalalignment='top', horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.tight_layout()

        # =========================================================
        # BARPLOT
        # =========================================================




        fig11, axes1 = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
        fig11.suptitle("Win Percentage per Enemy Pokemon", fontsize=16, fontweight='bold')

        for i, starter in enumerate(index_starter):
            ax = axes1[i]
            df_starter = df_master_battles[df_master_battles['Starter'] == starter]

            wins_per_enemy = df_starter.groupby('Enemy_Pokemon')['Win'].sum()
            enemies_with_wins = wins_per_enemy[wins_per_enemy > 0].index
            df_starter_filtered = df_starter[df_starter['Enemy_Pokemon'].isin(enemies_with_wins)]
            sns.barplot(data=df_starter_filtered, x="Enemy_Pokemon", y="Win_Percentage",
                        color=colors_starter.get(starter, "black"), errorbar=None, ax=ax)

            ax.set_title(starter, fontsize=14, fontweight='bold', color=colors_starter.get(starter, "black"))
            ax.set_xlabel("Enemy Pokemon")
            ax.tick_params(axis='x', rotation=45)
            ax.grid(True, linestyle='--', alpha=0.5, axis='y')

            if i == 0:
                ax.set_ylabel("Win Rate (%)")
            else:
                ax.set_ylabel("")

        plt.tight_layout()

        fig12, axes2 = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
        fig12.suptitle("Mean and Standard Deviation of Residual HP per Enemy", fontsize=16, fontweight='bold')

        for i, starter in enumerate(index_starter):
            ax = axes2[i]

            df_starter = df_master_battles[df_master_battles['Starter'] == starter]

            wins_per_enemy = df_starter.groupby('Enemy_Pokemon')['Win'].sum()
            enemies_with_wins = wins_per_enemy[wins_per_enemy > 0].index
            df_starter_filtered = df_starter[df_starter['Enemy_Pokemon'].isin(enemies_with_wins)]

            sns.barplot(data=df_starter_filtered, x="Enemy_Pokemon", y="Left_HP",
                        color=colors_starter.get(starter, "black"), errorbar="sd", capsize=0.1, ax=ax)

            ax.set_title(starter, fontsize=14, fontweight='bold', color=colors_starter.get(starter, "black"))
            ax.set_xlabel("Enemy Pokemon")
            ax.tick_params(axis='x', rotation=45)
            ax.grid(True, linestyle='--', alpha=0.5, axis='y')

            if i == 0:
                ax.set_ylabel("Residual HP (Mean with SD bars)")
            else:
                ax.set_ylabel("")

        df_grouped = df_master_battles.groupby(["Starter", "Enemy_Pokemon"]).agg({
            "Win": "mean",
            "Left_HP": "mean",
            "Turns": "mean"
        }).reset_index()

        df_grouped = df_grouped.rename(columns={
            "Win": "Mean_Win",
            "Left_HP": "Mean_Left_HP",
            "Turns": "Mean_Turns"
        })

        df_grouped = df_grouped.merge(
            df_master_battles_described_turns["50%"].rename("Median_Turns"),
            on="Starter"
        )

        novice_mask = (
                df_grouped["Mean_Win"].between(0.7, 0.9) &
                (df_grouped["Mean_Left_HP"] > 50)
        )
        skilled_mask = (
                df_grouped["Mean_Win"].between(0.5, 0.7) &
                (df_grouped["Mean_Turns"] > df_grouped["Median_Turns"])
        )

        df_grouped["Mean_Win"] *= 100

        fig13, axes3 = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
        fig13.suptitle("Pokémon Suitable for Novice and Skilled Users", fontsize=16, fontweight='bold')


        for i, starter in enumerate(index_starter):
            ax = axes3[i]

            df_filtered = df_grouped[ (df_grouped["Starter"] == starter) & (novice_mask | skilled_mask) ]
            colors = []
            for idx, row in df_filtered.iterrows():
                if novice_mask.loc[idx]:
                    colors.append("limegreen")
                elif skilled_mask.loc[idx]:
                    colors.append("dodgerblue")
            sns.barplot(
                data=df_filtered,
                x="Enemy_Pokemon",
                y="Mean_Win",
                hue="Enemy_Pokemon",
                palette=colors,
                dodge=False,
                legend=False,
                errorbar=None,
                ax=ax
            )
            ax.set_title(starter, fontsize=14, fontweight='bold', color=colors_starter.get(starter, "black"))
            ax.set_xlabel("Enemy Pokemon")
            ax.tick_params(axis='x', rotation=45)
            ax.grid(True, linestyle='--', alpha=0.5, axis='y')

            if i == 0:
                ax.set_ylabel("Win Rate %")
            else:
                ax.set_ylabel("")

        plt.tight_layout()
        '''

        plt.show()







