import random
from Database import MovesDatabase as Mdb
from Database import PkTypesDatabase as PkT_db
from Database import ItemsDb as Item_db

class PokemonTrainerClass:
    def __init__(self, name, pk_list, pk_active_index, items):
        self.name = name
        self.pk_list = pk_list
        self.pk_active_index = pk_active_index
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

    def use_change_pokemon(self, pokemon):
        for index, pk in enumerate(self.pk_list):
            if pk.name == pokemon.name:
                self.pk_active_index = index

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
        canheal = True
        for pk in self.pk_list:
            if pk.name == pokemon.name:
                start_hp = pk.currentHP
                if start_hp == pk.stats["hp"]:
                    print(f"You can't further heal that pokemon!")
                    canheal =  False
                else:
                    pk.currentHP += heal.effect
                    #chek if the healing goes above the maximum hp
                    if pk.currentHP > pk.stats["hp"]:
                        pk.currentHP = pk.stats["hp"]
                    print(f"{self.name} use {heal.name} on {pk.name} healing {pk.currentHP-start_hp} HP")
                    canheal = True
        return False, canheal

    def use_pokeball(self, pokeball):
        return True


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
    def use_move(self, move, opponent):
        # reduces the pp of the move
        if move.pp > 0:
            print(f"{self.name} uses {move.name} against {opponent.name}!")
            move.pp -= 1
        else:
            print(f"{move.name} can't use {move.name}!")

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
                    return True

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
            if effectiveness == 0.5:
                print(f"{move} is NOT MUCH EFFECTIVE on {opponent.name}!")
            elif effectiveness == 2.0:
                print(f"{move} is SUPER EFFECTIVE on {opponent.name}!")
            print(f"{opponent.name} takes {damage} HP damage.")
            print(f"HP left of {opponent.name}: {opponent.currentHP}")
            return True

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
            if move.type in PkT_db.TYPE_CHART:
                if t in PkT_db.TYPE_CHART[move.type]:
                    eff = eff * PkT_db.TYPE_CHART[move.type][t]
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

class PokemonBase:
    def __init__(self,pokedex_number, name, types, base_stats,moves):
        self.pokedex_number = pokedex_number
        self.name = name
        self.types = types
        self.base_stats = base_stats
        self.moves = moves

#creates a playable pokémon
    def create_playable_pokemon(self, level):
        stats_copy = dict(self.base_stats)
        current_hp = int(stats_copy["hp"])
        move_objects = [Mdb.MovesList[name].move_copy() for name in self.moves]
        return PokemonCharacterClass(
            name= self.name,
            level=level,
            types=self.types,
            stats=stats_copy,
            moves=move_objects,
            modifiers={
            "attack": 0,
            "defense": 0,
            "speed": 0,
            "special": 0,
            "accuracy": 0,
            },
            currentHP=current_hp
        )

