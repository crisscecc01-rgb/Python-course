import random
from math import floor

import Database as Db
import BaseClasses


class PokemonTrainerClass:
    def __init__(self, name, pk_list, pk_active_index, items, random_stats):
        self.name = name
        self.pk_list = pk_list
        self.pk_active_index = pk_active_index
        self.items = items  # dictionary of list of items {"heal": list_of_heals, "pokeballs": list_of_pokeballs}
        self.random_stats = random_stats
        self.num_battles = 10
    def str_pkList(self):
        nomi = [item.name for item in self.pk_list]
        string = ", ".join(nomi)

        return f"[ {string} ]"

    def str_items(self):
        string = ""
        for items in self.items:
            string = string + str(self.items[items]) + "\n"
        return string

    def str_stats(self):
        string = ""
        for stats, value in self.random_stats.items():
            string = string + str(f"{stats}:{value}") + "\n"
        return string

    def __str__(self):
         string = (f"{self.name} has {len(self.pk_list)} Pokemon: {self.str_pkList()} \n"
                   f"{self.name} has the following items: \n{self.str_items()}"
                   f"{self.name} has the following stats: \n{self.str_stats()}")
         return string

    def __repr__(self):
        return str(self)


    def use_change_pokemon(self, pokemon):
        for index, pk in enumerate(self.pk_list):
            if pk.name == pokemon.name:
                if self.pk_active_index == index:
                    print(f"The pokemon is already on the field!")
                    return False, False
                elif self.pk_list[index].currentHP == 0:
                    print(f"The pokemon is exhausted!")
                    return False, False
                else:
                    self.pk_active_index = index
                    print(f"Go {self.pk_list[index].name}!")
                    return False, True

    def ChoosePokemonAlive(self):
        list_index_alive = []
        for index, pokemon in enumerate(self.pk_list):
            if pokemon.currentHP > 0:
                print(f"{index + 1} Pokemon available: {self.pk_list[index]}")
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

    def RandomPokemonAlive(self):
        list_index_alive = []
        for index, pokemon in enumerate(self.pk_list):
            if pokemon.currentHP > 0:
                list_index_alive.append(index + 1)
        if not list_index_alive:
            return -1
        else:
            choice = random.randint(0, len(list_index_alive) - 1)
            return list_index_alive[choice]

    def use_heal(self, pokemon, heal):
        can_heal = True
        for pk in self.pk_list:
            if pk.name == pokemon.name:
                start_hp = pk.currentHP
                if start_hp == pk.stats["hp"]:
                    print(f"You can't further heal that pokemon!")
                    can_heal =  False
                else:
                    pk.currentHP += heal.effect
                    #chek if the healing goes above the maximum hp
                    if pk.currentHP > pk.stats["hp"]:
                        pk.currentHP = pk.stats["hp"]
                    print(f"{self.name} use 1 {heal.name} on {pk.name} healing {pk.currentHP-start_hp} HP")
                    if heal.number >= 1:
                        heal.number -= 1
                    else:
                        print(f"No more {heal.name} available")
                        self.items["heals"].remove(heal)
                    can_heal = True
        return False, can_heal

    def use_pokeball(self, pokeball, enemy_pokemon):
        can_use_pk =  True
        catch_rate_update = pokeball.catch_rate * (1 - enemy_pokemon.currentHP/self.pk_list[self.pk_active_index].currentHP)
        if random.random() < catch_rate_update:
            print(f"{self.name} caught a wild {enemy_pokemon.name}")
            self.pk_list.append(enemy_pokemon)
            if pokeball.number > 1:
                pokeball.number -= 1
            else:
                print(f"No more {pokeball.name} available")
                self.items["pokeballs"].remove(pokeball)
            return True, can_use_pk
        else:
            print(f"Unlucky: Wild {enemy_pokemon.name} exit the pokeball")
            if pokeball.number > 1:
                pokeball.number -= 1
            else:
                print(f"No more {pokeball.name} available")
                self.items["pokeballs"].remove(pokeball)
            return False, can_use_pk

class PokemonCharacterClass:
    def __init__(self, name, level, types, stats, modifiers, moves, currentHP, analytics_pk):
        self.name = name
        self.level = level
        self.types = types
        self.stats = stats
        self.modifiers = modifiers
        self.moves = moves
        self.currentHP = currentHP
        self.analytics_pk = analytics_pk

    def __str__(self):
        string = f"{self.name} --> [level={self.level} | types={self.types} | HP={self.currentHP}]"
        return string

    # function used to apply status or damage from a move
    def use_move(self, move, opponent):
        # reduces the pp of the move
        if move.name == "struggle":
            print(f"{self.name} uses {move.name} against {opponent.name}!")
        elif move.pp > 0:
            move.pp -= 1
            print(f"{self.name} uses {move.name} against {opponent.name}!")
        else:
            print(f"{self.name} can't use {move.name}!")
            return False, False


        # check if the move is a status move or a damage move
        if move.category == "status":
            modifierIndex = 0
            # check the target of the status move
            if move.effect["target_stat"][0] == "self":
                # modification of the modifiers attribute
                for stat in move.effect["target_stat"][1:]:
                    # check the boundaries
                    if self.modifiers[stat] > 5:
                        print(f"{stat} of {self.name} can't increase any further!")
                    elif self.modifiers[stat] < -5:
                        print(f"{stat} of {self.name} can't decrease any further!")
                    else:
                        # apply the status
                        self.modifiers[stat] = self.modifiers[stat] + move.effect["change"][modifierIndex]

                        if move.effect["change"][modifierIndex] > 0:
                            print(f"{stat} of {self.name} increased!")
                        else:
                            print(f"{stat} of {self.name} decreased!")
                        modifierIndex = modifierIndex + 1
            # same procedure in case the target is the opponent
            else:
                # Accuracy check
                if random.random() > move.accuracy:
                    print("\nBut it failed!")
                    return False, True

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
            if effectiveness == 0:
                print(f"{move.name} has NO EFFECT on {opponent.name}!")
            if effectiveness == 0.5:
                print(f"{move.name} is NOT MUCH EFFECTIVE on {opponent.name}!")
            elif effectiveness == 2.0:
                print(f"{move.name} is SUPER EFFECTIVE on {opponent.name}!")
            print(f"{opponent.name} takes {damage} HP damage.")
            #print(f"HP left of {opponent.name}: {opponent.currentHP}")
            return False, True

    def use_move_random(self, move, opponent):
        # check if the move is a status move or a damage move
        if move.category == "status":
            modifierIndex = 0
            # check the target of the status move
            if move.effect["target_stat"][0] == "self":
                # modification of the modifiers attribute
                for stat in move.effect["target_stat"][1:]:
                    # check the boundaries
                    if self.modifiers[stat] > 5:
                        pass
                    elif self.modifiers[stat] < -5:
                        pass
                    else:
                        # apply the status
                        self.modifiers[stat] = self.modifiers[stat] + move.effect["change"][modifierIndex]

                        if move.effect["change"][modifierIndex] > 0:
                            pass
                        else:
                            pass
                        modifierIndex = modifierIndex + 1
            # same procedure in case the target is the opponent
            else:
                # Accuracy check
                if random.random() > move.accuracy:
                    pass
                    return False, True

                for stat in move.effect["target_stat"][1:]:
                    if opponent.modifiers[stat] > 5:
                        pass
                    elif opponent.modifiers[stat] < -5:
                        pass
                    else:
                        opponent.modifiers[stat] = opponent.modifiers[stat] + move.effect["change"][modifierIndex]
                        if move.effect["change"][modifierIndex] > 0:
                            pass
                        else:
                            pass
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

            self.analytics_pk["pk_move"] = move.name
            self.analytics_pk["pk_damage"] = damage

            if opponent.currentHP <= 0:
                opponent.analytics_pk["pk_move"] = ""
                opponent.analytics_pk["pk_damage"] = 0

            return False, True
    # get the modified stats from the applied status to the Pk
    def get_modified_stat(self, stat):
        if self.modifiers[stat] >= 0:
            return self.stats[stat] * (self.modifiers[stat] + 2) / 2
        else:
            return self.stats[stat] * 2 / (2 - self.modifiers[stat])

    # evaluate the total modifiers for the damage evaluation
    def calc_modifier(self, move, opponent):
        stab = self.calc_stab(move)
        effectiveness = self.calc_effectiveness(move, opponent)
        crit, is_crit = self.calc_critical()
        luck = self.calc_luck()
        modifier = stab * effectiveness * crit * luck
        return modifier, is_crit, effectiveness

    # evaluate the STAB (same type attack boost)
    def calc_stab(self, move):
        return 1.5 if move.type in self.types else 1.0

    # check if the move is super effective or not
    @staticmethod
    def calc_effectiveness(move, opponent):
        eff = 1.0
        for t in opponent.types:
            if move.type in Db.Pt_db.TYPE_CHART:
                if t.lower() in Db.Pt_db.TYPE_CHART[move.type]:
                    eff = eff * Db.Pt_db.TYPE_CHART[move.type][t.lower()]
                else:
                    # print(f"Opponent type ({opponent.types}) in not registered for effectiveness evaluation")
                    eff *= 1
            else:
                # print(f"Chosen move type ({move.type}) is not registered for effectiveness evaluation")
                eff *= 1
        return eff

    # random critical hit, based on the user speed
    def calc_critical(self):
        crit_chance = self.stats["speed"] / 512
        is_crit = random.random() < crit_chance
        return (2.0 if is_crit else 1.0), is_crit

    # random roll between 0,85 and 1
    @staticmethod
    def calc_luck():
        return random.uniform(0.85, 1.0)

def create_playable_pokemon(name_pokemon, level):
    # i'm selecting the raw from the dataframe
    row = Db.P_db.Pokemon_df.loc[Db.P_db.Pokemon_df["display_name"] == name_pokemon].iloc[0]
    # creating the Move objects
    move_objects = [
        BaseClasses.move_copy(Db.M_db.MoveList_df.loc[move_name])
        for move_name in row["moves"]
    ]
    #this way the stats are adjusted only when the pokemon is created (if the pokemon level increment is added this should be modified)
    scaled_stats = scale_stats(row["base_stats"], level)

    analytics_pk = {"pk_hp": 0,
                    "pk_move": "",
                    "pk_damage": 0}
    return PokemonCharacterClass(
        row["display_name"],      # name
        level,                    # level
        row["types"],             # types
        scaled_stats,        # base stats
        {"attack": 0, "defense": 0, "speed": 0, "special": 0},  # in battle modifiers
        move_objects,             # Moves
        scaled_stats["hp"], # Hp init
        analytics_pk
    )
def scale_stats(base_stats, level):
    scaled_stats= {}

    for stat, value in base_stats.items():
        if stat == "hp":
            scaled_stats[stat] = floor(value*2*level/100)+5
        else:
            scaled_stats[stat] = floor(value*2*level/100)+level+10
    return scaled_stats






