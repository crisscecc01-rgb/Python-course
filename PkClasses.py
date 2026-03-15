from dataclasses import dataclass
from types import MappingProxyType
import random

@dataclass(frozen=True)
class PokemonBase:
    pokedex_number: int
    name: str
    types: tuple
    base_stats: MappingProxyType
    moves: tuple

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
                print(f"{self.name} uses {move.name} against {opponent.name}!")
                move.pp -= 1
            else:
                print(f"{self.name} can't use {move.name}!")

        # Accuracy check
        if random.random() > move.accuracy:
            print("\nBut it failed!")
            return
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
            if move.type in TYPE_CHART:
                if t in TYPE_CHART[move.type]:
                    eff = eff*TYPE_CHART[move.type][t]
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


#class used to define a move
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



#list of effectivness, every type has its effective dictionary associated
TYPE_CHART = {
    "normal": {
        "rock": 0.5, "ghost": 0, "steel": 0  
    },
    "fire": {
        "fire": 0.5, "water": 0.5, "grass": 2, "ice": 2, "bug": 2,
        "rock": 0.5, "dragon": 0.5
    },
    "water": {
        "fire": 2, "water": 0.5, "grass": 0.5, "ground": 2,
        "rock": 2, "dragon": 0.5
    },
    "grass": {
        "fire": 0.5, "water": 2, "grass": 0.5, "poison": 0.5,
        "ground": 2, "flying": 0.5, "bug": 0.5, "rock": 2,
        "dragon": 0.5
    },
    "electric": {
        "water": 2, "grass": 0.5, "electric": 0.5,
        "ground": 0, "flying": 2, "dragon": 0.5
    },
    "ice": {
        "fire": 0.5, "water": 0.5, "ice": 0.5,
        "grass": 2, "ground": 2, "flying": 2, "dragon": 2
    },
    "fighting": {
        "normal": 2, "ice": 2, "rock": 2,
        "poison": 0.5, "flying": 0.5, "psychic": 0.5,
        "bug": 0.5, "ghost": 0
    },
    "poison": {
        "grass": 2, "poison": 0.5, "ground": 0.5,
        "rock": 0.5, "ghost": 0.5
    },
    "ground": {
        "fire": 2, "electric": 2, "grass": 0.5,
        "poison": 2, "flying": 0, "bug": 0.5,
        "rock": 2
    },
    "flying": {
        "grass": 2, "electric": 0.5, "fighting": 2,
        "bug": 2, "rock": 0.5
    },
    "psychic": {
        "fighting": 2, "poison": 2,
        "psychic": 0.5
    },
    "bug": {
        "grass": 2, "psychic": 2,
        "fire": 0.5, "fighting": 0.5, "poison": 2,
        "flying": 0.5, "ghost": 0.5
    },
    "rock": {
        "fire": 2, "ice": 2, "flying": 2, "bug": 2,
        "fighting": 0.5, "ground": 0.5
    },
    "ghost": {
        "ghost": 2, "psychic": 0  
    },
    "dragon": {
        "dragon": 2
    }
}

#defined moves, only damage moves and status moves
MovesList = {
    "tackle": Move("tackle", "normal", "physical", 35, 0.95, 35, None),
    "razor leaf": Move("razor leaf", "grass", "physical", 55, 0.95, 25, None),
    "ember": Move("ember", "fire", "special", 40, 1.0, 25, None),
    "water gun": Move("water gun", "water", "special", 40, 1.0, 25, None),
    "growl": Move("growl", "normal", "status", None, 1.0, 40, effect={"target_stat": ["opponent","attack",], "change": [-1,]}),
    "tail wip": Move("tail wip", "normal", "status", None, 1.0, 40, effect={"target_stat": ["opponent", "defense",], "change": [-1,]}),
    "growth": Move("growth", "normal", "status", None, 1.0, 40, effect={"target_stat": ["self", "attack", "defense"], "change": [+1, +1]})
}


BulbasaurBase = PokemonBase(
    pokedex_number = 1,
    name="Bulbasaur",
    types=("Grass", "Poison"),
    base_stats=MappingProxyType({
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "speed": 45,
        "special": 65
    }),
    moves=("tackle", "razor leaf", "growl", "growth")
)
CharmanderBase = PokemonBase(
    pokedex_number=4,
    name="Charmander",
    types=("fire",),
    base_stats=MappingProxyType({
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "speed": 65,
        "special": 50
    }),
    moves=("tackle", "ember", "tail wip")
)
SquirtleBase = PokemonBase(
    pokedex_number=7,
    name="Squirtle",
    types=("water",),
    base_stats=MappingProxyType({
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "special": 50
    }),
    moves=("tackle", "water gun", "growl")
)
RattataBase = PokemonBase(
    pokedex_number=19,
    name="Rattata",
    types=("normal",),
    base_stats=MappingProxyType({
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "speed": 40,
        "special": 35
    }),
    moves=("tackle",)
)

PokemonList = [BulbasaurBase, CharmanderBase, SquirtleBase, RattataBase]