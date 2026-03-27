from PKGame import *
from PkClasses import *
from Database import PokemonDatabase as Pk_db
import PokemonStory



if __name__ == "__main__":
    PokemonStory.BeginStory()

    '''
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
        '''
