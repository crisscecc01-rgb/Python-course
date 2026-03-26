# main.py
from PKGame import *
from PkClasses import *
from Database import PokemonDatabase as Pk_db


def main():
    print("welcome in Pokémon simulator!")
    trainer_name = input("what's your name: ")

    trainer = PokemonTrainerClass(trainer_name, [], [])

    print("Select your starter pokémon:")
    starterPokemon = [create_playable_pokemon(Pk_db.PokemonList[0], 5), create_playable_pokemon(Pk_db.PokemonList[2], 5),create_playable_pokemon(Pk_db.PokemonList[4], 5)]
    for pokemon, opt in enumerate(starterPokemon):
        print(pokemon + 1, ':', opt.name)
    choice = (input("> "))

    while not choice.isdigit() or int(choice) <1 or int(choice) > len(starterPokemon):
        print("Select between 1 and " + str(len(starterPokemon)) + ":" )
        choice = (input("> "))
        for pokemon, opt in enumerate(starterPokemon):
            print(pokemon + 1, ':', opt.name)



    trainer.pk_list.append(starterPokemon[int(choice)-1])

    #print(trainer.pk_list)
    print(f"you selected {trainer.pk_list[0].name}!")
    
    enemy = PokemonTrainerClass("Gennaro Bullo", [create_playable_pokemon(Pk_db.PokemonList[18], 5)], [])
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
