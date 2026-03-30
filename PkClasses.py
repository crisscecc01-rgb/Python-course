import random
from types import MappingProxyType

from Database import MovesDatabase as Mdb
from Database import PkTypesDatabase as PkT_db
from Database import ItemsDb as Item_db

class PokemonTrainerClass:
    def __init__(self, name, pk_list, items):
        self.name = name
        self.pk_list = pk_list
        self.items = items

    def str_pkList(self):
        nomi = [item.name for item in self.pk_list]
        string = ", ".join(nomi)

        return f"[ {string} ]"

    def str_items(self):
        string = ""
        for items in self.items:
            string = string + str(self.items[items]) + "\n"
        return string

    def __str__(self):
         string = (f"{self.name} has {len(self.pk_list)} Pokemon: {self.str_pkList()} \n"
                   f"{self.name} has the following items: \n{self.str_items()}\n ")
         return string

    def __repr__(self):
        return str(self)

    def use_item(self):

        def use_heals(heals_list):
            print("Which heal do you want to use?:")
            for idx,heal in enumerate(heals_list):
                print(f"{idx+1} : you have {heal.number} {heal.name} ( --> +{heal.effect}) available")
            heal_choice = (input("> "))

            while not heal_choice.isdigit() or int(heal_choice) < 1 or int(heal_choice) > len(heals_list):
                print("Which heal do you want to use?:")
                for idx, heal in enumerate(heals_list):
                    print(f"{idx+1} : you have {heal.number} {heal.name} ( --> +{heal.effect}) available")
                heal_choice = (input("> "))

            heal_choice = int(heal_choice)-1
            print(f" {self.name} uses one {heals_list[heal_choice].name} of {heals_list[heal_choice].number} available")
            if heals_list[heal_choice].number > 1:
                heals_list[heal_choice].number = heals_list[heal_choice].number - 1
            else :
                heals_list.remove(heals_list[heal_choice])
            return heals_list[heal_choice].effect


        def use_pokeballs(pokeball):
            pass

        print("Which types of items do you want to use?:")
        index = 1
        for number in self.items:
            print(index, ':', number)
            index += 1
        choice = (input("> "))

        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.items):
            print("Which types of items do you want to use?:")
            index = 1
            for number in self.items:
                print(index, ':', number)
                index += 1
            choice = (input("> "))

        if choice == "1":
            return use_heals(self.items["heals"])
        elif choice == "2":
            return use_pokeballs(self.items["pokeballs"])
        return 0

class Move:
    def __init__(self, name, move_type, category, power, accuracy, pp, effect):
        self.name = name
        self.type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

    def move_copy(self):
        return Move(
            self.name,
            self.type,
            self.category,
            self.power,
            self.accuracy,
            self.pp,
            effect=self.effect.copy() if self.effect else None
        )

class HealClass:
    def __init__(self, name, number):
        self.name = name
        self.effect = Item_db.heals_dict[name]
        self.number = number

    def __str__(self):
        return f"{self.number} x {self.name} (--> +{self.effect})"
    def __repr__(self):
        return str(self)

class PokeBallClass:
    def __init__(self, name, number):
        self.name = name
        self.effect = Item_db.pokeball_dict[name]
        self.number = number

    def __str__(self):
        return f"{self.number} x {self.name} (--> {self.effect})"

    def __repr__(self):
        return str(self)

class PokemonCharacterClass:
    def __init__(self, name, level, types, stats, modifiers, moves, currentHP):
        self.name = name
        self.level = level
        self.types = types
        self.stats = stats
        self.modifiers = modifiers
        self.moves = moves
        self.currentHP = currentHP

    def __str__(self):
        string = f"{self.name} --> [level={self.level} | types={self.types} | HP={self.currentHP}]"
        return string

    # function used to apply status or damage from a move
    def use_move(self, move, opponent, ):
        #check if the move is in the move pool
        if move in self.moves:
            #reduces the pp of the move
            if move.pp > 0:
                print(f"{self.name} uses {move.name} against {opponent.name}!")
                move.pp -= 1
            else:
                print(f"{self.name} can't use {move.name}!")


        #check if the move is a status move or a damage move
        if move.category == "status":
            modifierIndex = 0
            #check the target of the status move
            if move.effect["target_stat"][0] == "self":
                #modification of the modifiers attribute
                for stat in move.effect["target_stat"][1:]:
                    #check the boundaries
                    if self.modifiers[stat] > 5:
                        print(f"{stat} of {self.name} can't increase any further!")
                    elif self.modifiers[stat] < -5:
                        print(f"{stat} of {self.name} can't decrease any further!")
                    else:
                        #apply the status
                        self.modifiers[stat] = self.modifiers[stat] + move.effect["change"][modifierIndex]
                        
                        if move.effect["change"][modifierIndex] > 0:
                            print(f"{stat} of {self.name} increased!")
                        else:
                            print(f"{stat} of {self.name} decreased!")
                        modifierIndex = modifierIndex + 1
            #same procedure in case the target is the opponent
            else:
                # Accuracy check
                if random.random() > move.accuracy:
                    print("\nBut it failed!")
                    return

                for stat in move.effect["target_stat"][1:]:
                    if opponent.modifiers[stat] > 5:
                        print(f"{stat} of {opponent.name} can't increase any further!")
                    elif opponent.modifiers[stat] < -5:
                        print(f"{stat} of {opponent.name} can't decrease any further!")
                    else:
                        opponent.modifiers[stat] = opponent.modifiers[stat] + move.effect["change"][modifierIndex]
                        if move.effect["change"][modifierIndex] > 0:
                            print(f"{stat} of {opponent.name} increased!")
                        else:
                            print(f"{stat} of {opponent.name} decreased!")
                        modifierIndex = modifierIndex + 1

        else:
            # Choose correct attack/defense stat
            if move.category == "physical":
                attack = self.get_modified_stat("attack")
                defense = opponent.get_modified_stat("defense")
            else:
                attack = self.get_modified_stat("special")
                defense = opponent.get_modified_stat("special")
            modifier, is_crit, effectiveness = self.calc_modifier(move, opponent)
            # Damage formula
            base = ((2 * self.level + 10) / 250) * (attack / defense) * move.power + 2
            damage = int(base * modifier)

            # Apply damage
            opponent.currentHP = max(0, opponent.currentHP - damage)

            # Messages
            if is_crit:
                print("critical hit!")
            if effectiveness == 0.5 :
                print(f"{move} is NOT MUCH EFFECTIVE on {opponent.name}!")
            elif effectiveness == 2.0 :
                print(f"{move} is SUPER EFFECTIVE on {opponent.name}!")
            print(f"{opponent.name} takes {damage} HP damage.")
            print(f"HP left of {opponent.name}: {opponent.currentHP}")

    #get the modified stats from the applied status to the Pk
    def get_modified_stat(self, stat):
        if self.modifiers[stat] >= 0:
            return self.stats[stat]*(self.modifiers[stat] + 2)/2
        else:
            return self.stats[stat]*(2)/(2 - self.modifiers[stat])

    # evaluate the total modifiers for the damage evaluation
    def calc_modifier(self, move, opponent):
        stab = self.calc_stab(move)
        effectiveness = self.calc_effectiveness(move, opponent)
        crit, is_crit = self.calc_critical()
        luck = self.calc_luck()
        modifier = stab*effectiveness*crit*luck
        return modifier, is_crit, effectiveness

    #evaluate the STAB (same type attack boost)
    def calc_stab(self, move):
        return 1.5 if move.type in self.types else 1.0

    #check if the move is super effective or not
    @staticmethod
    def calc_effectiveness(move, opponent):
        eff = 1.0
        for t in opponent.types:
            if move.type in PkT_db.TYPE_CHART:
                if t in PkT_db.TYPE_CHART[move.type]:
                    eff = eff * PkT_db.TYPE_CHART[move.type][t]
                else:
                    #print(f"Opponent type ({opponent.types}) in not registered for effectiveness evaluation")
                    eff*= 1
            else:
                #print(f"Chosen move type ({move.type}) is not registered for effectiveness evaluation")
                eff*= 1
        return eff
    #random critical hit, based on the user speed
    def calc_critical(self):
        crit_chance = self.stats["speed"] / 512
        is_crit = random.random() < crit_chance
        return (2.0 if is_crit else 1.0), is_crit
    #random roll between 0,85 and 1
    @staticmethod
    def calc_luck():
        return random.uniform(0.85, 1.0)

class PokemonBase:
    def __init__(self,pokedex_number, name, types, base_stats,moves):
        self.pokedex_number = pokedex_number
        self.name = name
        self.types = types
        self.base_stats = base_stats
        self.moves = moves

#creates a playable pokémon
def create_playable_pokemon(base, level):
    stats_copy = dict(base.base_stats)
    current_hp = int(stats_copy["hp"])
    move_objects = [Mdb.MovesList[name].move_copy() for name in base.moves]
    return PokemonCharacterClass(
        name= base.name,
        level=level,
        types=base.types,
        stats=stats_copy,
        moves=move_objects,
        modifiers={
        "attack": 0,
        "defense": 0,
        "speed": 0,
        "special": 0
        },
        currentHP=current_hp
    )

#function to select a move
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