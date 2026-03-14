from PkClasses import *

def create_playable_pokemon(base, level):
    stats_copy = dict(base.base_stats)
    current_hp = int(stats_copy["hp"])
    move_objects = [MovesList[name] for name in base.moves]
    return PokemonCharacterClass(
        name= base.name,
        level=level,
        types=base.types,
        stats=stats_copy,
        moves=move_objects,
        currentHP=current_hp
    )

def move_selection(userPk):
    print("Select a move:")
    i = 0
    for move in userPk.moves:
        i = i + 1
        print(str(i) + ")", move.name)
    choice = input("> ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(userPk.moves):
        print("Select between 1 and " + str(len(userPk.moves)) + ":")
        i = 0
        for move in userPk.moves:
            i = i + 1
            print(str(i) + ")", move.name)
        choice = (input("> "))
    return userPk.moves[int(choice) - 1]


def show_HUD(UserPk, opponent):
    print(f"{opponent.name} current hp: {opponent.currentHP}")
    print(f"{UserPk.name}  current hp: {UserPk.currentHP}")
    return move_selection(UserPk)

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

                return 0

