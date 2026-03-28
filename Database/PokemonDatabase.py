from types import MappingProxyType
from dataclasses import dataclass

@dataclass
class PokemonBase:
    pokedex_number: int
    name: str
    types: tuple
    base_stats: MappingProxyType
    moves: tuple

PokemonList = [
    PokemonBase(
        pokedex_number=1,
        name="Bulbasaur",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "speed": 45,
            "special": 65
        }),
        moves=('razor wind', 'swords dance', 'cut', 'bind')
    ),
    PokemonBase(
        pokedex_number=2,
        name="Ivysaur",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 62,
            "defense": 63,
            "speed": 60,
            "special": 80
        }),
        moves=('swords dance', 'cut', 'bind', 'vine whip')
    ),
    PokemonBase(
        pokedex_number=3,
        name="Venusaur",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 82,
            "defense": 83,
            "speed": 80,
            "special": 100
        }),
        moves=('swords dance', 'cut', 'bind', 'vine whip')
    ),
    PokemonBase(
        pokedex_number=4,
        name="Charmander",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "speed": 65,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=5,
        name="Charmeleon",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 64,
            "defense": 58,
            "speed": 80,
            "special": 80
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=6,
        name="Charizard",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 84,
            "defense": 78,
            "speed": 100,
            "special": 109
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=7,
        name="Squirtle",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 48,
            "defense": 65,
            "speed": 43,
            "special": 50
        }),
        moves=('mega punch', 'ice punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=8,
        name="Wartortle",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 63,
            "defense": 80,
            "speed": 58,
            "special": 65
        }),
        moves=('mega punch', 'ice punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=9,
        name="Blastoise",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 79,
            "attack": 83,
            "defense": 100,
            "speed": 78,
            "special": 85
        }),
        moves=('mega punch', 'ice punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=10,
        name="Caterpie",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 35,
            "speed": 45,
            "special": 20
        }),
        moves=('tackle', 'string shot', 'snore', 'bug bite')
    ),
    PokemonBase(
        pokedex_number=11,
        name="Metapod",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 20,
            "defense": 55,
            "speed": 30,
            "special": 25
        }),
        moves=('string shot', 'harden', 'iron defense', 'bug bite')
    ),
    PokemonBase(
        pokedex_number=12,
        name="Butterfree",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 50,
            "speed": 70,
            "special": 90
        }),
        moves=('razor wind', 'gust', 'whirlwind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=13,
        name="Weedle",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 35,
            "defense": 30,
            "speed": 50,
            "special": 20
        }),
        moves=('poison sting', 'string shot', 'bug bite', 'electroweb')
    ),
    PokemonBase(
        pokedex_number=14,
        name="Kakuna",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 25,
            "defense": 50,
            "speed": 35,
            "special": 25
        }),
        moves=('string shot', 'harden', 'iron defense', 'bug bite')
    ),
    PokemonBase(
        pokedex_number=15,
        name="Beedrill",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 40,
            "speed": 75,
            "special": 45
        }),
        moves=('swords dance', 'cut', 'headbutt', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=16,
        name="Pidgey",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 40,
            "speed": 56,
            "special": 35
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=17,
        name="Pidgeotto",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 63,
            "attack": 60,
            "defense": 55,
            "speed": 71,
            "special": 50
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=18,
        name="Pidgeot",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 83,
            "attack": 80,
            "defense": 75,
            "speed": 101,
            "special": 70
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=19,
        name="Rattata",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 56,
            "defense": 35,
            "speed": 72,
            "special": 25
        }),
        moves=('cut', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=20,
        name="Raticate",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 81,
            "defense": 60,
            "speed": 97,
            "special": 50
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=21,
        name="Spearow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 60,
            "defense": 30,
            "speed": 70,
            "special": 31
        }),
        moves=('razor wind', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=22,
        name="Fearow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 65,
            "speed": 100,
            "special": 61
        }),
        moves=('razor wind', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=23,
        name="Ekans",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 60,
            "defense": 44,
            "speed": 55,
            "special": 40
        }),
        moves=('bind', 'slam', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=24,
        name="Arbok",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 95,
            "defense": 69,
            "speed": 80,
            "special": 65
        }),
        moves=('bind', 'slam', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=25,
        name="Pikachu",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 55,
            "defense": 40,
            "speed": 90,
            "special": 50
        }),
        moves=('mega punch', 'pay day', 'thunder punch', 'slam')
    ),
    PokemonBase(
        pokedex_number=26,
        name="Raichu",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 90,
            "defense": 55,
            "speed": 110,
            "special": 90
        }),
        moves=('mega punch', 'pay day', 'thunder punch', 'slam')
    ),
    PokemonBase(
        pokedex_number=27,
        name="Sandshrew",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 75,
            "defense": 85,
            "speed": 40,
            "special": 20
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=28,
        name="Sandslash",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 100,
            "defense": 110,
            "speed": 65,
            "special": 45
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=29,
        name="Nidoran-f",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 47,
            "defense": 52,
            "speed": 41,
            "special": 40
        }),
        moves=('scratch', 'cut', 'double kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=30,
        name="Nidorina",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 62,
            "defense": 67,
            "speed": 56,
            "special": 55
        }),
        moves=('scratch', 'cut', 'double kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=31,
        name="Nidoqueen",
        types=('Poison', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 92,
            "defense": 87,
            "speed": 76,
            "special": 75
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=32,
        name="Nidoran-m",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 46,
            "attack": 57,
            "defense": 40,
            "speed": 50,
            "special": 40
        }),
        moves=('cut', 'double kick', 'headbutt', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=33,
        name="Nidorino",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 72,
            "defense": 57,
            "speed": 65,
            "special": 55
        }),
        moves=('cut', 'double kick', 'headbutt', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=34,
        name="Nidoking",
        types=('Poison', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 81,
            "attack": 102,
            "defense": 77,
            "speed": 85,
            "special": 85
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=35,
        name="Clefairy",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 45,
            "defense": 48,
            "speed": 35,
            "special": 60
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=36,
        name="Clefable",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 70,
            "defense": 73,
            "speed": 60,
            "special": 95
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=37,
        name="Vulpix",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 41,
            "defense": 40,
            "speed": 65,
            "special": 50
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=38,
        name="Ninetales",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 73,
            "attack": 76,
            "defense": 75,
            "speed": 100,
            "special": 81
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=39,
        name="Jigglypuff",
        types=('Normal', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 45,
            "defense": 20,
            "speed": 20,
            "special": 45
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=40,
        name="Wigglytuff",
        types=('Normal', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 140,
            "attack": 70,
            "defense": 45,
            "speed": 45,
            "special": 85
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=41,
        name="Zubat",
        types=('Poison', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 35,
            "speed": 55,
            "special": 30
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=42,
        name="Golbat",
        types=('Poison', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 70,
            "speed": 90,
            "special": 65
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=43,
        name="Oddish",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 50,
            "defense": 55,
            "speed": 30,
            "special": 75
        }),
        moves=('swords dance', 'cut', 'headbutt', 'take down')
    ),
    PokemonBase(
        pokedex_number=44,
        name="Gloom",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 65,
            "defense": 70,
            "speed": 40,
            "special": 85
        }),
        moves=('swords dance', 'cut', 'headbutt', 'take down')
    ),
    PokemonBase(
        pokedex_number=45,
        name="Vileplume",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 85,
            "speed": 50,
            "special": 110
        }),
        moves=('swords dance', 'cut', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=46,
        name="Paras",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 70,
            "defense": 55,
            "speed": 25,
            "special": 45
        }),
        moves=('scratch', 'swords dance', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=47,
        name="Parasect",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 95,
            "defense": 80,
            "speed": 30,
            "special": 60
        }),
        moves=('scratch', 'swords dance', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=48,
        name="Venonat",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 55,
            "defense": 50,
            "speed": 45,
            "special": 40
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=49,
        name="Venomoth",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 65,
            "defense": 60,
            "speed": 90,
            "special": 90
        }),
        moves=('razor wind', 'gust', 'whirlwind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=50,
        name="Diglett",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 10,
            "attack": 55,
            "defense": 25,
            "speed": 95,
            "special": 35
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=51,
        name="Dugtrio",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 100,
            "defense": 50,
            "speed": 120,
            "special": 50
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=52,
        name="Meowth",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 35,
            "speed": 90,
            "special": 40
        }),
        moves=('pay day', 'scratch', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=53,
        name="Persian",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 70,
            "defense": 60,
            "speed": 115,
            "special": 65
        }),
        moves=('pay day', 'scratch', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=54,
        name="Psyduck",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 52,
            "defense": 48,
            "speed": 55,
            "special": 65
        }),
        moves=('mega punch', 'pay day', 'ice punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=55,
        name="Golduck",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 82,
            "defense": 78,
            "speed": 85,
            "special": 95
        }),
        moves=('mega punch', 'pay day', 'ice punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=56,
        name="Mankey",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 80,
            "defense": 35,
            "speed": 70,
            "special": 35
        }),
        moves=('karate chop', 'mega punch', 'pay day', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=57,
        name="Primeape",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 105,
            "defense": 60,
            "speed": 95,
            "special": 60
        }),
        moves=('karate chop', 'mega punch', 'pay day', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=58,
        name="Growlithe",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 70,
            "defense": 45,
            "speed": 60,
            "special": 70
        }),
        moves=('double kick', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=59,
        name="Arcanine",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 110,
            "defense": 80,
            "speed": 95,
            "special": 100
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=60,
        name="Poliwag",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 50,
            "defense": 40,
            "speed": 90,
            "special": 40
        }),
        moves=('pound', 'double slap', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=61,
        name="Poliwhirl",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 65,
            "defense": 65,
            "speed": 90,
            "special": 50
        }),
        moves=('pound', 'double slap', 'mega punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=62,
        name="Poliwrath",
        types=('Water', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 95,
            "defense": 95,
            "speed": 70,
            "special": 70
        }),
        moves=('pound', 'double slap', 'mega punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=63,
        name="Abra",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 25,
            "attack": 20,
            "defense": 15,
            "speed": 90,
            "special": 105
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=64,
        name="Kadabra",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 35,
            "defense": 30,
            "speed": 105,
            "special": 120
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=65,
        name="Alakazam",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 50,
            "defense": 45,
            "speed": 120,
            "special": 135
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=66,
        name="Machop",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 80,
            "defense": 50,
            "speed": 35,
            "special": 35
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=67,
        name="Machoke",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 100,
            "defense": 70,
            "speed": 45,
            "special": 50
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=68,
        name="Machamp",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 130,
            "defense": 80,
            "speed": 55,
            "special": 65
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=69,
        name="Bellsprout",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 75,
            "defense": 35,
            "speed": 40,
            "special": 70
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=70,
        name="Weepinbell",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 50,
            "speed": 55,
            "special": 85
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=71,
        name="Victreebel",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 105,
            "defense": 65,
            "speed": 70,
            "special": 100
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=72,
        name="Tentacool",
        types=('Water', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 35,
            "speed": 70,
            "special": 50
        }),
        moves=('swords dance', 'cut', 'bind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=73,
        name="Tentacruel",
        types=('Water', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 70,
            "defense": 65,
            "speed": 100,
            "special": 80
        }),
        moves=('swords dance', 'cut', 'bind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=74,
        name="Geodude",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 80,
            "defense": 100,
            "speed": 20,
            "special": 30
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=75,
        name="Graveler",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 95,
            "defense": 115,
            "speed": 35,
            "special": 45
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=76,
        name="Golem",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 130,
            "speed": 45,
            "special": 55
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=77,
        name="Ponyta",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 85,
            "defense": 55,
            "speed": 90,
            "special": 65
        }),
        moves=('stomp', 'double kick', 'headbutt', 'horn drill')
    ),
    PokemonBase(
        pokedex_number=78,
        name="Rapidash",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 100,
            "defense": 70,
            "speed": 105,
            "special": 80
        }),
        moves=('pay day', 'swords dance', 'stomp', 'double kick')
    ),
    PokemonBase(
        pokedex_number=79,
        name="Slowpoke",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 65,
            "defense": 65,
            "speed": 15,
            "special": 40
        }),
        moves=('pay day', 'stomp', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=80,
        name="Slowbro",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 75,
            "defense": 110,
            "speed": 30,
            "special": 100
        }),
        moves=('mega punch', 'pay day', 'ice punch', 'stomp')
    ),
    PokemonBase(
        pokedex_number=81,
        name="Magnemite",
        types=('Electric', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 25,
            "attack": 35,
            "defense": 70,
            "speed": 45,
            "special": 95
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=82,
        name="Magneton",
        types=('Electric', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 60,
            "defense": 95,
            "speed": 70,
            "special": 120
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=83,
        name="Farfetchd",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 52,
            "attack": 90,
            "defense": 55,
            "speed": 60,
            "special": 58
        }),
        moves=('razor wind', 'swords dance', 'cut', 'gust')
    ),
    PokemonBase(
        pokedex_number=84,
        name="Doduo",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 85,
            "defense": 45,
            "speed": 75,
            "special": 35
        }),
        moves=('swords dance', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=85,
        name="Dodrio",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 110,
            "defense": 70,
            "speed": 110,
            "special": 60
        }),
        moves=('swords dance', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=86,
        name="Seel",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 45,
            "defense": 55,
            "speed": 45,
            "special": 45
        }),
        moves=('pay day', 'slam', 'headbutt', 'horn drill')
    ),
    PokemonBase(
        pokedex_number=87,
        name="Dewgong",
        types=('Water', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 70,
            "defense": 80,
            "speed": 70,
            "special": 70
        }),
        moves=('pay day', 'headbutt', 'horn drill', 'body slam')
    ),
    PokemonBase(
        pokedex_number=88,
        name="Grimer",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 50,
            "speed": 25,
            "special": 40
        }),
        moves=('pound', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=89,
        name="Muk",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 105,
            "defense": 75,
            "speed": 50,
            "special": 65
        }),
        moves=('pound', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=90,
        name="Shellder",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 65,
            "defense": 100,
            "speed": 40,
            "special": 45
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=91,
        name="Cloyster",
        types=('Water', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 95,
            "defense": 180,
            "speed": 70,
            "special": 85
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=92,
        name="Gastly",
        types=('Ghost', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 35,
            "defense": 30,
            "speed": 80,
            "special": 100
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=93,
        name="Haunter",
        types=('Ghost', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 50,
            "defense": 45,
            "speed": 95,
            "special": 115
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=94,
        name="Gengar",
        types=('Ghost', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 65,
            "defense": 60,
            "speed": 110,
            "special": 130
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=95,
        name="Onix",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 45,
            "defense": 160,
            "speed": 70,
            "special": 30
        }),
        moves=('bind', 'slam', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=96,
        name="Drowzee",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 48,
            "defense": 45,
            "speed": 42,
            "special": 43
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=97,
        name="Hypno",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 73,
            "defense": 70,
            "speed": 67,
            "special": 73
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=98,
        name="Krabby",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 105,
            "defense": 90,
            "speed": 50,
            "special": 25
        }),
        moves=('vice grip', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=99,
        name="Kingler",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 130,
            "defense": 115,
            "speed": 75,
            "special": 50
        }),
        moves=('vice grip', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=100,
        name="Voltorb",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 50,
            "speed": 100,
            "special": 55
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=101,
        name="Electrode",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 70,
            "speed": 150,
            "special": 80
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=102,
        name="Exeggcute",
        types=('Grass', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 40,
            "defense": 80,
            "speed": 40,
            "special": 60
        }),
        moves=('swords dance', 'headbutt', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=103,
        name="Exeggutor",
        types=('Grass', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 95,
            "defense": 85,
            "speed": 55,
            "special": 125
        }),
        moves=('swords dance', 'stomp', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=104,
        name="Cubone",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 95,
            "speed": 35,
            "special": 40
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=105,
        name="Marowak",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 80,
            "defense": 110,
            "speed": 45,
            "special": 50
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=106,
        name="Hitmonlee",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 120,
            "defense": 53,
            "speed": 87,
            "special": 35
        }),
        moves=('mega punch', 'swords dance', 'double kick', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=107,
        name="Hitmonchan",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 105,
            "defense": 79,
            "speed": 76,
            "special": 35
        }),
        moves=('comet punch', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=108,
        name="Lickitung",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 55,
            "defense": 75,
            "speed": 30,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=109,
        name="Koffing",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 65,
            "defense": 95,
            "speed": 35,
            "special": 60
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=110,
        name="Weezing",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 120,
            "speed": 60,
            "special": 85
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=111,
        name="Rhyhorn",
        types=('Ground', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 85,
            "defense": 95,
            "speed": 25,
            "special": 30
        }),
        moves=('swords dance', 'stomp', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=112,
        name="Rhydon",
        types=('Ground', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 130,
            "defense": 120,
            "speed": 40,
            "special": 45
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=113,
        name="Chansey",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 250,
            "attack": 5,
            "defense": 5,
            "speed": 50,
            "special": 35
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=114,
        name="Tangela",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 55,
            "defense": 115,
            "speed": 60,
            "special": 100
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=115,
        name="Kangaskhan",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 95,
            "defense": 80,
            "speed": 90,
            "special": 40
        }),
        moves=('pound', 'comet punch', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=116,
        name="Horsea",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 40,
            "defense": 70,
            "speed": 60,
            "special": 70
        }),
        moves=('razor wind', 'headbutt', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=117,
        name="Seadra",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 65,
            "defense": 95,
            "speed": 85,
            "special": 95
        }),
        moves=('headbutt', 'take down', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=118,
        name="Goldeen",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 67,
            "defense": 60,
            "speed": 63,
            "special": 35
        }),
        moves=('swords dance', 'headbutt', 'horn attack', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=119,
        name="Seaking",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 92,
            "defense": 65,
            "speed": 68,
            "special": 65
        }),
        moves=('swords dance', 'headbutt', 'horn attack', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=120,
        name="Staryu",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 45,
            "defense": 55,
            "speed": 85,
            "special": 70
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=121,
        name="Starmie",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 75,
            "defense": 85,
            "speed": 115,
            "special": 100
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=122,
        name="Mr-mime",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 65,
            "speed": 90,
            "special": 100
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=123,
        name="Scyther",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 110,
            "defense": 80,
            "speed": 105,
            "special": 55
        }),
        moves=('razor wind', 'swords dance', 'cut', 'wing attack')
    ),
    PokemonBase(
        pokedex_number=124,
        name="Jynx",
        types=('Ice', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 50,
            "defense": 35,
            "speed": 95,
            "special": 115
        }),
        moves=('pound', 'double slap', 'mega punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=125,
        name="Electabuzz",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 83,
            "defense": 57,
            "speed": 105,
            "special": 95
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=126,
        name="Magmar",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 95,
            "defense": 57,
            "speed": 93,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=127,
        name="Pinsir",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 125,
            "defense": 100,
            "speed": 85,
            "special": 55
        }),
        moves=('vice grip', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=128,
        name="Tauros",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 100,
            "defense": 95,
            "speed": 110,
            "special": 40
        }),
        moves=('stomp', 'headbutt', 'horn attack', 'horn drill')
    ),
    PokemonBase(
        pokedex_number=129,
        name="Magikarp",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 10,
            "defense": 55,
            "speed": 80,
            "special": 15
        }),
        moves=('tackle', 'hydro pump', 'splash', 'flail')
    ),
    PokemonBase(
        pokedex_number=130,
        name="Gyarados",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 125,
            "defense": 79,
            "speed": 81,
            "special": 60
        }),
        moves=('bind', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=131,
        name="Lapras",
        types=('Water', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 130,
            "attack": 85,
            "defense": 80,
            "speed": 60,
            "special": 85
        }),
        moves=('headbutt', 'horn drill', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=132,
        name="Ditto",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 48,
            "defense": 48,
            "speed": 48,
            "special": 48
        }),
        moves=('transform',)
    ),
    PokemonBase(
        pokedex_number=133,
        name="Eevee",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 50,
            "speed": 55,
            "special": 45
        }),
        moves=('pay day', 'double kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=134,
        name="Vaporeon",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 130,
            "attack": 65,
            "defense": 60,
            "speed": 65,
            "special": 110
        }),
        moves=('pay day', 'double kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=135,
        name="Jolteon",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 65,
            "defense": 60,
            "speed": 130,
            "special": 110
        }),
        moves=('pay day', 'double kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=136,
        name="Flareon",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 130,
            "defense": 60,
            "speed": 65,
            "special": 95
        }),
        moves=('pay day', 'double kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=137,
        name="Porygon",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 60,
            "defense": 70,
            "speed": 40,
            "special": 85
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=138,
        name="Omanyte",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 40,
            "defense": 100,
            "speed": 35,
            "special": 90
        }),
        moves=('bind', 'slam', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=139,
        name="Omastar",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 60,
            "defense": 125,
            "speed": 55,
            "special": 115
        }),
        moves=('bind', 'sand attack', 'headbutt', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=140,
        name="Kabuto",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 80,
            "defense": 90,
            "speed": 55,
            "special": 55
        }),
        moves=('scratch', 'sand attack', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=141,
        name="Kabutops",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 115,
            "defense": 105,
            "speed": 80,
            "special": 65
        }),
        moves=('scratch', 'razor wind', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=142,
        name="Aerodactyl",
        types=('Rock', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 105,
            "defense": 65,
            "speed": 130,
            "special": 60
        }),
        moves=('razor wind', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=143,
        name="Snorlax",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 160,
            "attack": 110,
            "defense": 65,
            "speed": 30,
            "special": 65
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=144,
        name="Articuno",
        types=('Ice', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 85,
            "defense": 100,
            "speed": 85,
            "special": 95
        }),
        moves=('razor wind', 'gust', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=145,
        name="Zapdos",
        types=('Electric', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 90,
            "defense": 85,
            "speed": 100,
            "special": 125
        }),
        moves=('razor wind', 'whirlwind', 'fly', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=146,
        name="Moltres",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 100,
            "defense": 90,
            "speed": 90,
            "special": 125
        }),
        moves=('razor wind', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=147,
        name="Dratini",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 64,
            "defense": 45,
            "speed": 50,
            "special": 50
        }),
        moves=('bind', 'slam', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=148,
        name="Dragonair",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 84,
            "defense": 65,
            "speed": 70,
            "special": 70
        }),
        moves=('bind', 'slam', 'headbutt', 'horn drill')
    ),
    PokemonBase(
        pokedex_number=149,
        name="Dragonite",
        types=('Dragon', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 134,
            "defense": 95,
            "speed": 80,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=150,
        name="Mewtwo",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 106,
            "attack": 110,
            "defense": 90,
            "speed": 130,
            "special": 154
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=151,
        name="Mew",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('pound', 'mega punch', 'pay day', 'fire punch')
    ),
]
