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
    def __init__(self, name, level, types, stats, moves, currentHP):
        self.name = name
        self.level = level
        self.types = types
        self.stats = stats
        self.moves = moves
        self.currentHP = currentHP

    def use_move(self, move, opponent, ):

        if move in self.moves:
            if move.pp > 0:
                print(f"{self.name} uses {move.name} against {opponent.name}!")
                move.pp -= 1
            else:
                print(f"{self.name} can't use {move.name}!")

        # Accuracy check
        if random.random() > move.accuracy:
            print("\nBut it failed!")
            return

        # Choose correct attack/defense stat
        if move.category == "physical":
            attack = self.stats["attack"]
            defense = opponent.stats["defense"]
        else:
            attack = self.stats["special"]
            defense = opponent.stats["special"]
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


    def calc_modifier(self, move, opponent):
        stab = self.calc_stab(move)
        effectiveness = self.calc_effectiveness(move, opponent)
        crit, is_crit = self.calc_critical()
        luck = self.calc_luck()
        modifier = stab*effectiveness*crit*luck
        return modifier, is_crit, effectiveness


    def calc_stab(self, move):
        return 1.5 if move.type in self.types else 1.0

    @staticmethod
    def calc_effectiveness(move, opponent):
        eff = 1.0
        for t in opponent.types:
            if move.type in TYPE_CHART:
                if t in TYPE_CHART[move.type]:
                    eff = eff*TYPE_CHART[move.type][t]
                else:
                    print(f"Opponent type ({opponent.types}) in not registered for effectiveness evaluation")
                    eff*= 1
            else:
                print(f"Chosen move type ({move.type}) is not registered for effectiveness evaluation")
                eff*= 1
        return eff

    def calc_critical(self):
        crit_chance = self.stats["speed"] / 512
        is_crit = random.random() < crit_chance
        return (2.0 if is_crit else 1.0), is_crit

    @staticmethod
    def calc_luck():
        return random.uniform(0.85, 1.0)



class Move:
    def __init__(self, name, move_type, category, power, accuracy, pp):
        self.name = name
        self.type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp



TYPE_CHART = { "fire" : {"fire" : 0.5, "water" : 2, "grass" : 2 } ,
 "grass" : {"fire" : 0.5, "water" : 2, "grass" : 0.5 },
 "water" : {"fire" : 2, "water" : 0.5, "grass" : 0.5 } }



MovesList = {
    "tackle": Move("tackle", "normal", "physical", 35, 0.5, 35),
    "razor leaf": Move("razor leaf", "grass", "physical", 55, 0.95, 25),
    "ember": Move("ember", "fire", "special", 40, 1.0, 25),
    "water gun": Move("water gun", "water", "special", 40, 0.5, 25)
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
    moves=("tackle", "razor leaf")
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
    moves=("tackle", "ember")
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
    moves=("tackle", "water gun")
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