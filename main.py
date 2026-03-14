# main.py
import random
from PKGame import *
from PkClasses import *

def main():
    print("welcome in Pokémon simulator!")
    trainer_name = input("what's your name: ")

    trainer = PokemonTrainerClass(trainer_name, [], [])

    print("Select your starter pokémon:")
    for pokemon, opt in enumerate(PokemonList):
        print(pokemon + 1, ':', opt.name)
    choice = (input("> "))

    while not choice.isdigit() or int(choice) <1 or int(choice) > len(PokemonList):
        print("Select between 1 and " + str(len(PokemonList)) + ":" )
        for pokemon, opt in enumerate(PokemonList):
            print(pokemon + 1, ':', opt.name)
        choice = (input("> "))
    if choice == "1":
        trainer.pk_list.append(create_playable_pokemon(BulbasaurBase, 5))
    elif choice == "2":
        trainer.pk_list.append(create_playable_pokemon(CharmanderBase, 5))
    elif choice == "3":
        trainer.pk_list.append(create_playable_pokemon(SquirtleBase, 5))
    elif choice == "4":
        trainer.pk_list.append(create_playable_pokemon(RattataBase, 5))
    print(f"you selected {trainer.pk_list[0].name}!")
    
    enemy = PokemonTrainerClass("Gennaro Bullo", [create_playable_pokemon(RattataBase, 5)], [])
    EnemyPkIndex = 0
    UserPkIndex = 0
    print(f"Trainer battle starts against " + enemy.name)
    print(enemy.name + " sends on the field " + enemy.pk_list[EnemyPkIndex].name)
    print("go " + trainer.pk_list[UserPkIndex].name + "!")
    BattleResult = 0
    while  BattleResult == 0:
       BattleResult = pk_battle(trainer, enemy, 0, 0)

    if BattleResult == 1:
        print(f"you've won the battle")
    elif BattleResult == 2:
        print(f"you've lost the battle")



if __name__ == "__main__":
    main()
