import random

from fontTools.ttLib.tables.otTables import DeltaSetIndexMap

from Database import PkTypesDatabase as PkT_db

class PokemonTrainerClass:
    def __init__(self, name, pk_list, items):
        self.name = name
        self.pk_list = pk_list
        self.items = items

    def __str__(self):
        return f"{self.name} has {len(self.pk_list)} Pokemon and {len(self.items)} items."
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


# function used to apply status or damage from a move
    def use_move(self, move, opponent, ):
        #check if the move is in the move pool
        if move in self.moves:
            #reduces the pp of the move
            if move.pp > 0:
                if move.category == "status":
                    print(f"{self.name} uses {move.name}!")
                else:
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
            # Accuracy check
            if random.random() > move.accuracy:
                print("\nBut it failed!")
                return
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

