# main.py
import random
from PkClasses import (
    TrainerClass, CharacterClass,
    BulbasaurBase, CharmanderBase, SquirtleBase, RattataBase,
    MovesList, PokemonList
)

def create_playable_pokemon(base, level):
    stats_copy = dict(base.BaseStats)
    current_hp = int(stats_copy["hp"])
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

def show_HUD(UserPk, opponent):
    print(f"{opponent.Name} current hp: {opponent.CurrentHP}")
    print(f"{UserPk.Name}  current hp: {UserPk.CurrentHP}")
    return MoveSelection(UserPk)



def PkBattle(character, enemy, UserPkIndex, EnemyPkIndex):
    SelectedMove = show_HUD(character.PkList[UserPkIndex], enemy.PkList[EnemyPkIndex])
    #speed check
    if character.PkList[UserPkIndex].Stats["speed"] >  enemy.PkList[EnemyPkIndex].Stats["speed"]:
        character.PkList[UserPkIndex].useMove(SelectedMove, enemy.PkList[EnemyPkIndex])
        
        if enemy.PkList[EnemyPkIndex].CurrentHP == 0:
            print(f"{enemy.PkList[EnemyPkIndex].Name} has no HP left")
            return 1
        else:
            
            OpponentMove = enemy.PkList[EnemyPkIndex].Moves[int(random.random()*len(enemy.PkList[EnemyPkIndex].Moves))]
            enemy.PkList[EnemyPkIndex].useMove(OpponentMove, character.PkList[UserPkIndex])
           
            if character.PkList[UserPkIndex].CurrentHP == 0:
                print(f"{character.PkList[UserPkIndex].Name} has no HP left")
                return 2
            else:
                print(f"{character.PkList[UserPkIndex].Name} has {character.PkList[UserPkIndex].CurrentHP} left")
                return 0
    else:
        OpponentMove = enemy.PkList[EnemyPkIndex].Moves[int(random.random()*len(enemy.PkList[EnemyPkIndex].Moves))]
        enemy.PkList[EnemyPkIndex].useMove(OpponentMove, character.PkList[UserPkIndex])
       
        if character.PkList[UserPkIndex].CurrentHP == 0:
            print(f"{character.PkList[UserPkIndex].Name} has no HP left")
            return 2
        else:
            
            character.PkList[UserPkIndex].useMove(SelectedMove, enemy.PkList[EnemyPkIndex])
           
            if  enemy.PkList[EnemyPkIndex].CurrentHP == 0:
                print(f"{ enemy.PkList[EnemyPkIndex].Name} has no HP left")
                return 1
            else:
               
                return 0
                    


def main():
    print("welcome in Pokémon simulator!")
    trainer_name = input("what's your name: ")

    trainer = TrainerClass(trainer_name, [], [])

    print("Select your starter pokémon:")
    for pokémon, opt in enumerate(PokemonList):
        print(pokémon + 1, ':', opt.Name)
    choice = (input("> "))

    while not choice.isdigit() or int(choice) <1 or int(choice) > len(PokemonList):
        print("Select between 1 and " + str(len(PokemonList)) + ":" )
        for pokémon, opt in enumerate(PokemonList):
            print(pokémon + 1, ':', opt.Name)
        choice = (input("> "))
    if choice == "1":
        trainer.PkList.append(create_playable_pokemon(BulbasaurBase, 5))
    elif choice == "2":
        trainer.PkList.append(create_playable_pokemon(CharmanderBase, 5))
    elif choice == "3":
        trainer.PkList.append(create_playable_pokemon(SquirtleBase, 5))
    elif choice == "4":
        trainer.PkList.append(create_playable_pokemon(RattataBase, 5))
    print(f"you selected {trainer.PkList[0].Name}!")
    
    enemy = TrainerClass("Gennaro Bullo", [create_playable_pokemon(RattataBase, 5)], [])
    EnemyPkIndex = 0;
    UserPkIndex = 0;
    print(f"Trainer battle starts against " + enemy.Name)
    print(enemy.Name + " sends on the field " + enemy.PkList[EnemyPkIndex].Name)
    print("go " + trainer.PkList[UserPkIndex].Name + "!")
    BattleResult = 0
    while  BattleResult == 0:
       BattleResult = PkBattle(trainer, enemy, 0, 0)

    if BattleResult == 1:
        print(f"you've won the battle")
    elif BattleResult == 2:
        print(f"you've lost the battle")



if __name__ == "__main__":
    main()
