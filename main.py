import PokemonStory
import numpy
import pprint
import json

if __name__ == "__main__":
    number_cycles = 29
    story = {"Bulbasaur": [],
             "Charmander": [],
             "Squirtle": []}
    end_story = None
    print("Want to randomize? (y/n)")
    choice = input("> ").strip().lower()

    if choice == "y":
        for i in range(number_cycles):
            print(f"{i}")
            if i <= round((number_cycles-1)/3)*1:
                PokemonStory.BeginStory("1",i,story,choice, number_cycles)
            if round((number_cycles - 1) / 3)*1+1 <= i <= round((number_cycles - 1) / 3)*2:
                PokemonStory.BeginStory("2",i,story,choice, number_cycles)
            if round((number_cycles - 1) / 3)*2+1 <= i <= round((number_cycles - 1) / 3)*3:
                PokemonStory.BeginStory("3",i,story,choice, number_cycles)
    elif choice == "n":
        i=1
        PokemonStory.BeginStory("1", i, story, choice, number_cycles)

    print("\n--- Simulation result (story) ---")
    #pprint.pprint(story, indent=4)
    #print(json.dumps(story, indent=4))

    # --- Stampa personalizzata e leggibile della variabile story ---
    print("\n\n" + "=" * 5)
    print(" SIMULATION REPORT ".center(50, "="))
    print("=" * 50)

    for starter, simulazioni in story.items():
        print(f"\n🌟 STARTER: {starter} (simulation total number: {len(simulazioni)})")
        print("-" * 50)

        if not simulazioni:
            print("  No simulation registered.")
            continue

        # Iteriamo sulle simulazioni, mostrandone solo alcune per non intasare la console
        for index, stats in enumerate(simulazioni):
            # Mostriamo solo le prime 2 simulazioni per starter (puoi aumentare questo numero)
            if index >= 5:
                print(f"  ... e altre {len(simulazioni) - 2} simulazioni omesse per brevità ...")
                break

            # Calcoliamo qualche statistica rapida per la singola simulazione
            incontri_totali = len(stats["wild_pokemons"])
            vittorie = stats["win_loss"].count(1)
            sconfitte = stats["win_loss"].count(0)
            win_rate = (vittorie / incontri_totali * 100) if incontri_totali > 0 else 0

            print(f"  [Simulation n: {index + 1}]")
            print(f"    wild Pokémon encountered : {incontri_totali}")
            print(f"    Victories: {vittorie} | Losses: {sconfitte} | Win Rate: {win_rate:.1f}%")
            print(f"    Total number of turns: {stats['total_num_turns'][:5]}")

            # Mostriamo solo un assaggio degli HP rimasti (i primi 5 scontri)
            primi_hp = stats['left_hp'][:5]
            primi_pk = stats["wild_pokemons"][:5]
            if primi_hp:
                print(f"    % HP remaining in the first 5 turns: {primi_hp}")
                print(f"    Name of the battled pokémons in the first 5 turns: {primi_pk} ")
            print("")