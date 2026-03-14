from dataclasses import dataclass
from types import MappingProxyType
import random


TYPE_CHART = { "fire" : {"fire" : 0.5, "water" : 2, "grass" : 2 } ,
 "grass" : {"fire" : 0.5, "water" : 2, "grass" : 0.5 },
 "water" : {"fire" : 2, "water" : 0.5, "grass" : 0.5 } }


@dataclass(frozen=True)
class PokemonBase:
    PokedexNumber: int
    Name: str
    Types: tuple
    BaseStats: MappingProxyType
    Moves: tuple

class TrainerClass:
    def __init__(self, Name, PkList, Items):
        self.Name = Name
        self.PkList = PkList
        self.Items = Items

    def __str__(self, other):
        return f"{self.Name} has {len(self.PkList)} Pokemon and {len(self.Items)} items."
    def __repr__(self):
        return str(self)

print("trainer class loaded")
class CharacterClass:
    def __init__(self, Name, Level, Types, Stats, Moves, CurrentHP):
        self.Name = Name
        self.Level = Level
        self.Types = Types
        self.Stats = Stats
        self.Moves = Moves
        self.CurrentHP = CurrentHP

    def calc_stab(self, move):
        return 1.5 if move.type in self.Types else 1.0

    def calc_effectiveness(self, move, opponent):
        eff = 1.0
        for t in opponent.Types:
            if move.type in TYPE_CHART:
                if t in TYPE_CHART[move.type]:
                    eff = eff*TYPE_CHART[move.type][t]
                else:
                    eff*= 1
            else:
                eff*= 1
        return eff

    def calc_modifier(self, move, opponent):
        FirstModifier = self.calc_stab(move)
        SecondModifier = self.calc_effectiveness(move, opponent)
        ThirdModifier, is_crit = self.calc_critical()
        FourthModifier = self.calc_luck()
        Modifier = FirstModifier*SecondModifier*ThirdModifier*FourthModifier
        return Modifier, is_crit
        
    def calc_critical(self):
        crit_chance = self.Stats["speed"] / 512
        is_crit = random.random() < crit_chance
        return (2.0 if is_crit else 1.0), is_crit

    def calc_luck(self):
        return random.uniform(0.85, 1.0)

    def useMove(self, move, opponent,):
        print(f"{self.Name} uses {move.name}!")

        # Accuracy check
        if random.random() > move.accuracy:
            print("but it failed")
            return

        # Choose correct attack/defense stat
        if move.category == "physical":
            attack = self.Stats["attack"]
            defense = opponent.Stats["defense"]
        else:
            attack = self.Stats["special"]
            defense = opponent.Stats["special"]
        modifier, is_crit = self.calc_modifier(move, opponent)
        # Damage formula
        base = ((2 * self.Level + 10) / 250) * (attack / defense) * move.power + 2
        damage = int(base*modifier)

        # Apply damage
        opponent.CurrentHP = max(0, opponent.CurrentHP - damage)

        # Messages
        if is_crit:
            print("critical hit!")
        print(f"{opponent.Name} takes {damage} HP damage.")
        print(f"HP left of {opponent.Name}: {opponent.CurrentHP}")



print("character class loaded") 

class Move:
    def __init__(self, name, type_, category, power, accuracy, pp):
        self.name = name
        self.type = type_
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

print("character move loaded") 

MovesList = {
    "tackle": Move("tackle", "normal", "physical", 35, 0.95, 35),
    "razor leaf": Move("razor leaf", "grass", "physical", 55, 0.95, 25),
    "ember": Move("ember", "fire", "special", 40, 1.0, 25),
    "water gun": Move("water gun", "water", "special", 40, 1.0, 25)
}

BulbasaurBase = PokemonBase(
    PokedexNumber = 1,
    Name="Bulbasaur",
    Types=("Grass", "Poison"),
    BaseStats=MappingProxyType({
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "speed": 45,
        "special": 65
    }),
    Moves=("tackle", "razor leaf")
)
CharmanderBase = PokemonBase(
    PokedexNumber=4,
    Name="Charmander",
    Types=("fire",),
    BaseStats=MappingProxyType({
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "speed": 65,
        "special": 50
    }),
    Moves=("tackle", "ember")
)
SquirtleBase = PokemonBase(
    PokedexNumber=7,
    Name="Squirtle",
    Types=("water",),
    BaseStats=MappingProxyType({
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "special": 50
    }),
    Moves=("tackle", "water gun")
)
RattataBase = PokemonBase(
    PokedexNumber=19,
    Name="Rattata",
    Types=("normal",),
    BaseStats=MappingProxyType({
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "speed": 72,
        "special": 35
    }),
    Moves=("tackle",)
)

PokemonList = [BulbasaurBase, CharmanderBase, SquirtleBase, RattataBase]