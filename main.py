import PokemonStory
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns


if __name__ == "__main__":
    number_cycles = 31
    story = {"Bulbasaur": [],
             "Charmander": [],
             "Squirtle": []}
    end_story = None
    print("Want to randomize? (y/n)")
    choice = input("> ").strip().lower()

    if choice == "y":
        for i in range(number_cycles):
            print(f"{i}")
            if i < round((number_cycles-1)/3)*1:
                PokemonStory.BeginStory(list(story.keys())[0],story,choice)
            elif i < round((number_cycles - 1) / 3)*2:
                PokemonStory.BeginStory(list(story.keys())[1],story,choice)
            elif i < round((number_cycles - 1) / 3)*3:
                PokemonStory.BeginStory(list(story.keys())[2],story,choice)
    elif choice == "n":
        i=1
        PokemonStory.BeginStory("1", story, choice)

    '''
    df_win_loss_story = {}
    df_average_win_loss_story = {}
    df_cumSum_win_loss_story = {}
    dict_turns = {}
    df_turns = {}
    dict_hps = {}
    df_hps = {}
    records = []

    for starter, simulations in story.items():
        matrix_win_loss = []
        matrix_turns = []
        dict_turns[starter] = []
        dict_hps[starter] = []
        for sim in simulations:
            for i in range(len(sim["wild_pokemons"])):
                records.append({"Starter": starter,
                                "Enemy_Pokemon": sim["wild_pokemon"][sim][i],
                                "Win": sim["win_loss"][sim][i],
                                "Left_HP": sim["left_hp"][sim][i],})
            matrix_win_loss.append(sim["win_loss"])
            dict_turns[starter].extend(sim["total_num_turns"])
            dict_hps[starter].extend(sim["left_hp"])

        df_master = pd.DataFrame(records)
        df_wl = pd.DataFrame(matrix_win_loss)
        df_wl.index = [f"Game_{i+1}" for i in range(len(df_wl))]
        df_wl.columns = [f"Battle_{j+1}" for j in range(len(df_wl.columns))]
        df_win_loss_story[starter] = df_wl
        df_average_win_loss_story[starter] = df_wl.mean(axis=0)
        df_cumSum_win_loss_story[starter] = df_average_win_loss_story[starter].cumsum(axis=0)

    df_turns = pd.DataFrame(dict_turns)
    df_hps = pd.DataFrame(dict_hps)



    #print("DataFrame di Bulbasaur:")
    #print(df_win_loss_story["Bulbasaur"].to_string())

    #print("Average DataFrame di Bulbasaur:")
    #print(df_average_win_loss_story["Bulbasaur"].to_string())

    #print("Average DataFrame di Bulbasaur:")
    #print(df_cumSum_win_loss_story["Bulbasaur"].to_string())

    sns.set_theme()

    # SIMPLE PLOT
    plt.figure(1,figsize=(10, 5))
    colors_starter = {
        "Bulbasaur": "green",
        "Charmander": "red",
        "Squirtle": "blue"
    }
    for starter, series in df_cumSum_win_loss_story.items():
        color = colors_starter.get(starter,"black")
        plt.plot(series.index, series.values, label=starter, color=color, marker='o', linewidth=2)

    plt.title("Cumulative Average Victories per Starter", fontsize=14, fontweight='bold')
    plt.xlabel("Number of Battles", fontsize=12)
    plt.ylabel("Average Cumulative Victories", fontsize=12)
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
    plt.xticks(rotation=45)
    plt.legend(title="Starter Pokémon", fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()


    #BOX PLOT
    max_val_turns = max([max(turn) for turn in dict_turns.values()])

    plt.figure(2,figsize=(15, 5))
    conf = 131
    plt.suptitle("Distribution of Battle Lengths (Number of Turns)", fontsize=16, fontweight='bold')
    for starter, turn in dict_turns.items():
        plt.subplot(conf)
        color = colors_starter.get(starter,"black")
        box = plt.boxplot(dict_turns[starter], patch_artist=True, tick_labels=[starter])
        for patch in box['boxes']:
            patch.set_facecolor(color)
            patch.set_alpha(0.5)


        plt.ylim(0, max_val_turns + 1)
        plt.xlabel("Number of Turns in a Battle", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5, axis='y')
        stats = df_turns[starter].describe()
        testo = f"Mean: {stats.loc['mean']:.2f}\nMedian: {stats.loc['50%']:.2f}\n25%: {stats.loc['25%']:.2f}\n75%: {stats.loc['75%']:.2f}"
        plt.text(0.95, 0.95, testo, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        if conf == 131:
            plt.ylabel("Frequency (Density)", fontsize=12)
        conf+=1
    plt.tight_layout()



    # BOX PLOT
    plt.figure(3, figsize=(15, 5))
    conf = 131
    plt.suptitle("Distribution of Remaining HP at the End of Battles", fontsize=16, fontweight='bold')
    max_val_hp = max([max(hp) for hp in dict_hps.values() if hp])

    for starter, hp in dict_hps.items():
        plt.subplot(conf)
        color = colors_starter.get(starter, "black")

        box = plt.boxplot(dict_hps[starter], patch_artist=True, tick_labels=[starter])
        for patch in box['boxes']:
            patch.set_facecolor(color)
            patch.set_alpha(0.5)

        plt.ylim(0, max_val_hp + (max_val_hp * 0.1))
        plt.title(starter, fontsize=14, fontweight='bold', color=color)
        plt.xlabel("Remaining HP", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5, axis='y')
        stats = df_hps[starter].describe()
        testo = f"Mean: {stats.loc['mean']:.2f}\nMedian: {stats.loc['50%']:.2f}\n25%: {stats.loc['25%']:.2f}\n75%: {stats.loc['75%']:.2f}"
        plt.text(0.95, 0.95, testo, transform=plt.gca().transAxes, fontsize=10,
                 verticalalignment='top', horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        if conf == 131:
            plt.ylabel("Frequency (Density)", fontsize=12)
        conf += 1
    plt.tight_layout()
    
    
    plt.show()
    '''

    records = []
    for starter, simulations in story.items():
        for game_idx, sim in enumerate(simulations):
            num_battles = len(sim["wild_pokemons"])

            for i in range(num_battles):
                records.append({
                    "Starter": starter,
                    "Game": game_idx + 1,
                    "Battle_Number": i + 1,
                    "Enemy_Pokemon": sim["wild_pokemons"][i],
                    "Win": sim["win_loss"][i],
                    "Left_HP": sim["left_hp"][i],
                    "Turns": sim["total_num_turns"][i]
                })

    df_master = pd.DataFrame(records)
    print(df_master)

    sns.set_theme()
    colors_starter = {"Bulbasaur": "green", "Charmander": "red", "Squirtle": "blue"}

    # =========================================================
    # SIMPLE PLOT
    # =========================================================
    plt.figure(1, figsize=(10, 5))
    cumulative_wins = df_master.groupby(['Starter', 'Battle_Number'])['Win'].mean().groupby(
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
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(data=df_master, x="Starter", y="Turns", hue="Starter", palette=colors_starter, ax=axes[0])
    axes[0].set_title("Battle Lengths (Number of Turns)", fontweight='bold')

    sns.boxplot(data=df_master, x="Starter", y="Left_HP", hue="Starter", palette=colors_starter, ax=axes[1])
    axes[1].set_title("Remaining HP at End of Battle", fontweight='bold')

    plt.tight_layout()

    # =========================================================
    # BARPLOT
    # =========================================================

    df_master['Win_Percentage'] = df_master['Win'] * 100

    fig1, axes1 = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
    fig1.suptitle("Win Percentage per Enemy Pokemon", fontsize=16, fontweight='bold')

    for i, starter in enumerate(["Bulbasaur", "Charmander", "Squirtle"]):
        ax = axes1[i]
        df_starter = df_master[df_master['Starter'] == starter]

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

    fig2, axes2 = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
    fig2.suptitle("Mean and Standard Deviation of Residual HP per Enemy", fontsize=16, fontweight='bold')

    for i, starter in enumerate(["Bulbasaur", "Charmander", "Squirtle"]):
        ax = axes2[i]

        df_starter = df_master[df_master['Starter'] == starter]

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

    plt.tight_layout()

    plt.show()





