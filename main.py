# main.py

from PkClasses import (
    TrainerClass, CharacterClass,
    BulbasaurBase, CharmanderBase, SquirtleBase,
    MovesList, PokemonList
)

def create_playable_pokemon(base, level):
    stats_copy = dict(base.BaseStats)
    current_hp = stats_copy["hp"]*level/50
    move_objects = [MovesList[name] for name in base.Moves]

    return CharacterClass(
        Name=base.Name,
        Level=level,
        Types=base.Types,
        Stats=stats_copy,
        Moves=move_objects,
        CurrentHP=current_hp
    )

def MoveSelection(user):
    print("Select a move:")
    i = 0
    for move in user.Moves:
        i = i+1
        print(str(i) + ")", move.name)
    choice = input("> ")
    while  not choice.isdigit() or int(choice) <1 or int(choice) > len(user.Moves):
        print("Select between 1 and " + str(len(user.Moves)) + ":" )
        i = 0
        for move in user.Moves:
            i = i+1
            print(str(i) + ")", move.name)
        choice = (input("> "))
    return user.Moves[int(choice)-1]

def main():
    print("welcome in Pokémon simulator!")
    trainer_name = input("what's your name: ")

    trainer = TrainerClass(trainer_name, [], [])

    print("Select your starter pokémon:")
    for pokémon, opt in enumerate(PokemonList):
        print(pokémon + 1, ':', opt)
    choice = (input("> "))

    while not choice.isdigit() or int(choice) <1 or int(choice) > len(PokemonList):
        print("Select between 1 and " + str(len(PokemonList)) + ":" )
        for pokémon, opt in enumerate(PokemonList):
            print(pokémon + 1, ':', opt)
        choice = (input("> "))

    if choice == "1":
        trainer.PkList.append(create_playable_pokemon(BulbasaurBase, 5))
    elif choice == "2":
        trainer.PkList.append(create_playable_pokemon(CharmanderBase, 5))
    elif choice == "3":
        trainer.PkList.append(create_playable_pokemon(SquirtleBase, 5))

    print(f"you selected {trainer.PkList[0].Name}!")

    MoveSelection(trainer.PkList[0])

if __name__ == "__main__":
    main()
