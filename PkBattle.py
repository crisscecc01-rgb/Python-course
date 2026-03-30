import random
from matplotlib.transforms import BlendedAffine2D
import PkClasses



def move_selection(userPk):
    print("Select a move:")
    i = 0
    for move in userPk.moves:
        i = i + 1
        print(str(i) + ")", move.name, " pp: ", move.pp)
    choice = input("> ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(userPk.moves):
        print("Select between 1 and " + str(len(userPk.moves)) + ":")
        i = 0
        for move in userPk.moves:
            i = i + 1
            print(str(i) + ")", move.name, " pp: ", move.pp)
        choice = (input("> "))
    return userPk.moves[int(choice) - 1]

#shows a basic HUD of the battle
def show_HUD(UserPk, opponent):
    print(f"{opponent.name} current hp: {opponent.currentHP}")
    print(f"{UserPk.name}  current hp: {UserPk.currentHP}")
    #if move move_selection()
    #if item item_selection()
    return move_selection(UserPk)

#function which is used to generate a single battle turn. if the user loose it returns 2, if the user wins it returs 1, otherwise it returns 0
def pk_battle(trainer, enemy, UserPkIndex, EnemyPkIndex):
    selected_move = show_HUD(trainer.pk_list[UserPkIndex], enemy.pk_list[EnemyPkIndex])
    # speed check
    if trainer.pk_list[UserPkIndex].stats["speed"] > enemy.pk_list[EnemyPkIndex].stats["speed"]:
        trainer.pk_list[UserPkIndex].use_move(selected_move, enemy.pk_list[EnemyPkIndex])

        if enemy.pk_list[EnemyPkIndex].currentHP == 0:
            print(f"{enemy.pk_list[EnemyPkIndex].name} has no HP left")
            return 1
        else:

            opponent_move = enemy.pk_list[EnemyPkIndex].moves[int(random.random() * len(enemy.pk_list[EnemyPkIndex].moves))]
            enemy.pk_list[EnemyPkIndex].use_move(opponent_move, trainer.pk_list[UserPkIndex])

            if trainer.pk_list[UserPkIndex].currentHP == 0:
                print(f"{trainer.pk_list[UserPkIndex].name} has no HP left")
                return 2
            else:
                print(f"{trainer.pk_list[UserPkIndex].name} has {trainer.pk_list[UserPkIndex].currentHP} left")
                return 0
    else:
        opponent_move = enemy.pk_list[EnemyPkIndex].moves[int(random.random() * len(enemy.pk_list[EnemyPkIndex].moves))]
        enemy.pk_list[EnemyPkIndex].use_move(opponent_move, trainer.pk_list[UserPkIndex])

        if trainer.pk_list[UserPkIndex].currentHP == 0:
            print(f"{trainer.pk_list[UserPkIndex].name} has no HP left")
            return 2
        else:

            trainer.pk_list[UserPkIndex].use_move(selected_move, enemy.pk_list[EnemyPkIndex])

            if enemy.pk_list[EnemyPkIndex].currentHP == 0:
                print(f"{enemy.pk_list[EnemyPkIndex].name} has no HP left")
                return 1
            else:
                print(f"{enemy.pk_list[EnemyPkIndex].name} has {enemy.pk_list[EnemyPkIndex].currentHP} left")
                return 0

def pk_wild_battle(trainer, UserPkIndex, wild_pokemon):

    selected_move = show_HUD(trainer.pk_list[UserPkIndex], wild_pokemon)
    # speed check
    if trainer.pk_list[UserPkIndex].stats["speed"] > wild_pokemon.stats["speed"]:
        trainer.pk_list[UserPkIndex].use_move(selected_move, wild_pokemon)

        if wild_pokemon.currentHP == 0:
            print(f"{wild_pokemon.name} has no HP left")
            return 1
        else:

            opponent_move = wild_pokemon.moves[int(random.random() * len(wild_pokemon.moves))]
            wild_pokemon.use_move(opponent_move, trainer.pk_list[UserPkIndex])

            if trainer.pk_list[UserPkIndex].currentHP == 0:
                print(f"{trainer.pk_list[UserPkIndex].name} has no HP left")
                return 2
            else:
                print(f"{trainer.pk_list[UserPkIndex].name} has {trainer.pk_list[UserPkIndex].currentHP} left")
                return 0
    else:
        opponent_move = wild_pokemon.moves[int(random.random() * len(wild_pokemon.moves))]
        wild_pokemon.use_move(opponent_move, trainer.pk_list[UserPkIndex])

        if trainer.pk_list[UserPkIndex].currentHP == 0:
            print(f"{trainer.pk_list[UserPkIndex].name} has no HP left")
            return 2
        else:

            trainer.pk_list[UserPkIndex].use_move(selected_move, wild_pokemon)

            if wild_pokemon.currentHP == 0:
                print(f"{wild_pokemon.name} has no HP left")
                return 1
            else:
                print(f"{wild_pokemon.name} has {wild_pokemon.currentHP} left")
                return 0

def ChoosePokemonAlive(trainer):
    list_index_alive = []
    for index, pokemon in enumerate(trainer.pk_list):
        if pokemon.currentHP > 0:
            print(f"{index + 1} Pokemon available: {trainer.pk_list[index]}")
            list_index_alive.append(index + 1)
    if not list_index_alive:
        print("You have no pokemon alive!")
        return -1
    else:
        print("Chose your next pokemon")
        choice = input("> ").strip().lower()
        while not int(choice) in list_index_alive:
            print("Chose better")
            choice = input("> ").strip().lower()
        return int(choice) - 1

def RandomPokemonAlive(trainer):
    list_index_alive = []
    for index, pokemon in enumerate(trainer.pk_list):
        if pokemon.currentHP > 0:
            list_index_alive.append(index + 1)
    if not list_index_alive:
        return -1
    else:
        choice = random.randint(0, len(list_index_alive) - 1)
        return list_index_alive[choice]





