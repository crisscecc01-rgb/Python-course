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
    PokemonBase(
        pokedex_number=152,
        name="Chikorita",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 49,
            "defense": 65,
            "speed": 45,
            "special": 49
        }),
        moves=('swords dance', 'cut', 'vine whip', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=153,
        name="Bayleef",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 62,
            "defense": 80,
            "speed": 60,
            "special": 63
        }),
        moves=('swords dance', 'cut', 'vine whip', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=154,
        name="Meganium",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 82,
            "defense": 100,
            "speed": 80,
            "special": 83
        }),
        moves=('swords dance', 'cut', 'vine whip', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=155,
        name="Cyndaquil",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "speed": 65,
            "special": 60
        }),
        moves=('cut', 'double kick', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=156,
        name="Quilava",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 64,
            "defense": 58,
            "speed": 80,
            "special": 80
        }),
        moves=('cut', 'double kick', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=157,
        name="Typhlosion",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 84,
            "defense": 78,
            "speed": 100,
            "special": 109
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'cut')
    ),
    PokemonBase(
        pokedex_number=158,
        name="Totodile",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 64,
            "speed": 43,
            "special": 44
        }),
        moves=('mega punch', 'ice punch', 'scratch', 'razor wind')
    ),
    PokemonBase(
        pokedex_number=159,
        name="Croconaw",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 80,
            "defense": 80,
            "speed": 58,
            "special": 59
        }),
        moves=('mega punch', 'ice punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=160,
        name="Feraligatr",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 105,
            "defense": 100,
            "speed": 78,
            "special": 79
        }),
        moves=('mega punch', 'ice punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=161,
        name="Sentret",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 46,
            "defense": 34,
            "speed": 20,
            "special": 35
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=162,
        name="Furret",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 76,
            "defense": 64,
            "speed": 90,
            "special": 45
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=163,
        name="Hoothoot",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 30,
            "defense": 30,
            "speed": 50,
            "special": 36
        }),
        moves=('wing attack', 'whirlwind', 'fly', 'tackle')
    ),
    PokemonBase(
        pokedex_number=164,
        name="Noctowl",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 50,
            "defense": 50,
            "speed": 70,
            "special": 86
        }),
        moves=('wing attack', 'whirlwind', 'fly', 'tackle')
    ),
    PokemonBase(
        pokedex_number=165,
        name="Ledyba",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 20,
            "defense": 30,
            "speed": 55,
            "special": 40
        }),
        moves=('comet punch', 'mega punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=166,
        name="Ledian",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 35,
            "defense": 50,
            "speed": 85,
            "special": 55
        }),
        moves=('comet punch', 'mega punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=167,
        name="Spinarak",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 60,
            "defense": 40,
            "speed": 30,
            "special": 40
        }),
        moves=('body slam', 'double edge', 'poison sting', 'twineedle')
    ),
    PokemonBase(
        pokedex_number=168,
        name="Ariados",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 90,
            "defense": 70,
            "speed": 40,
            "special": 60
        }),
        moves=('swords dance', 'body slam', 'double edge', 'poison sting')
    ),
    PokemonBase(
        pokedex_number=169,
        name="Crobat",
        types=('Poison', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 90,
            "defense": 80,
            "speed": 130,
            "special": 70
        }),
        moves=('gust', 'wing attack', 'fly', 'double edge')
    ),
    PokemonBase(
        pokedex_number=170,
        name="Chinchou",
        types=('Water', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 38,
            "defense": 38,
            "speed": 67,
            "special": 56
        }),
        moves=('take down', 'double edge', 'supersonic', 'mist')
    ),
    PokemonBase(
        pokedex_number=171,
        name="Lanturn",
        types=('Water', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 125,
            "attack": 58,
            "defense": 58,
            "speed": 67,
            "special": 76
        }),
        moves=('take down', 'double edge', 'supersonic', 'mist')
    ),
    PokemonBase(
        pokedex_number=172,
        name="Pichu",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 40,
            "defense": 15,
            "speed": 60,
            "special": 35
        }),
        moves=('double slap', 'mega punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=173,
        name="Cleffa",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 25,
            "defense": 28,
            "speed": 15,
            "special": 45
        }),
        moves=('pound', 'mega punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=174,
        name="Igglybuff",
        types=('Normal', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 30,
            "defense": 15,
            "speed": 15,
            "special": 40
        }),
        moves=('pound', 'mega punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=175,
        name="Togepi",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 20,
            "defense": 65,
            "speed": 20,
            "special": 40
        }),
        moves=('pound', 'mega punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=176,
        name="Togetic",
        types=('Fairy', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 40,
            "defense": 85,
            "speed": 40,
            "special": 80
        }),
        moves=('pound', 'mega punch', 'fly', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=177,
        name="Natu",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 50,
            "defense": 45,
            "speed": 70,
            "special": 70
        }),
        moves=('double edge', 'leer', 'peck', 'drill peck')
    ),
    PokemonBase(
        pokedex_number=178,
        name="Xatu",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 75,
            "defense": 70,
            "speed": 95,
            "special": 95
        }),
        moves=('fly', 'double edge', 'leer', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=179,
        name="Mareep",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 40,
            "defense": 40,
            "speed": 35,
            "special": 65
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=180,
        name="Flaaffy",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 55,
            "defense": 55,
            "speed": 45,
            "special": 80
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=181,
        name="Ampharos",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 75,
            "defense": 85,
            "speed": 55,
            "special": 115
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=182,
        name="Bellossom",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 95,
            "speed": 50,
            "special": 90
        }),
        moves=('swords dance', 'cut', 'double edge', 'acid')
    ),
    PokemonBase(
        pokedex_number=183,
        name="Marill",
        types=('Water', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 20,
            "defense": 50,
            "speed": 40,
            "special": 20
        }),
        moves=('mega punch', 'ice punch', 'slam', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=184,
        name="Azumarill",
        types=('Water', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 50,
            "defense": 80,
            "speed": 50,
            "special": 60
        }),
        moves=('mega punch', 'ice punch', 'slam', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=185,
        name="Sudowoodo",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 100,
            "defense": 115,
            "speed": 30,
            "special": 30
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=186,
        name="Politoed",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 75,
            "defense": 75,
            "speed": 70,
            "special": 90
        }),
        moves=('pound', 'double slap', 'mega punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=187,
        name="Hoppip",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 35,
            "defense": 40,
            "speed": 50,
            "special": 35
        }),
        moves=('pay day', 'swords dance', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=188,
        name="Skiploom",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 45,
            "defense": 50,
            "speed": 80,
            "special": 45
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=189,
        name="Jumpluff",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 55,
            "defense": 70,
            "speed": 110,
            "special": 55
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=190,
        name="Aipom",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 70,
            "defense": 55,
            "speed": 85,
            "special": 40
        }),
        moves=('double slap', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=191,
        name="Sunkern",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 30,
            "defense": 30,
            "speed": 30,
            "special": 30
        }),
        moves=('swords dance', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=192,
        name="Sunflora",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 75,
            "defense": 55,
            "speed": 30,
            "special": 105
        }),
        moves=('pound', 'swords dance', 'cut', 'tackle')
    ),
    PokemonBase(
        pokedex_number=193,
        name="Yanma",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 65,
            "defense": 45,
            "speed": 95,
            "special": 75
        }),
        moves=('swords dance', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=194,
        name="Wooper",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 45,
            "defense": 45,
            "speed": 15,
            "special": 25
        }),
        moves=('ice punch', 'slam', 'double kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=195,
        name="Quagsire",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 85,
            "defense": 85,
            "speed": 35,
            "special": 65
        }),
        moves=('mega punch', 'ice punch', 'slam', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=196,
        name="Espeon",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 65,
            "defense": 60,
            "speed": 110,
            "special": 130
        }),
        moves=('pay day', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=197,
        name="Umbreon",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 65,
            "defense": 110,
            "speed": 65,
            "special": 60
        }),
        moves=('pay day', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=198,
        name="Murkrow",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 42,
            "speed": 91,
            "special": 85
        }),
        moves=('gust', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=199,
        name="Slowking",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 75,
            "defense": 80,
            "speed": 30,
            "special": 100
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=200,
        name="Misdreavus",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 60,
            "speed": 85,
            "special": 85
        }),
        moves=('headbutt', 'double edge', 'growl', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=201,
        name="Unown",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 72,
            "defense": 48,
            "speed": 48,
            "special": 72
        }),
        moves=('hidden power',)
    ),
    PokemonBase(
        pokedex_number=202,
        name="Wobbuffet",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 190,
            "attack": 33,
            "defense": 58,
            "speed": 33,
            "special": 33
        }),
        moves=('counter', 'amnesia', 'splash', 'destiny bond')
    ),
    PokemonBase(
        pokedex_number=203,
        name="Girafarig",
        types=('Normal', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 80,
            "defense": 65,
            "speed": 85,
            "special": 90
        }),
        moves=('razor wind', 'stomp', 'double kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=204,
        name="Pineco",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 90,
            "speed": 15,
            "special": 35
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=205,
        name="Forretress",
        types=('Bug', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 90,
            "defense": 140,
            "speed": 40,
            "special": 60
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=206,
        name="Dunsparce",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 70,
            "defense": 70,
            "speed": 45,
            "special": 65
        }),
        moves=('bind', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=207,
        name="Gligar",
        types=('Ground', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 75,
            "defense": 105,
            "speed": 85,
            "special": 35
        }),
        moves=('guillotine', 'razor wind', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=208,
        name="Steelix",
        types=('Steel', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 85,
            "defense": 200,
            "speed": 30,
            "special": 55
        }),
        moves=('cut', 'bind', 'slam', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=209,
        name="Snubbull",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 80,
            "defense": 50,
            "speed": 30,
            "special": 40
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=210,
        name="Granbull",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 120,
            "defense": 75,
            "speed": 45,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=211,
        name="Qwilfish",
        types=('Water', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 95,
            "defense": 85,
            "speed": 85,
            "special": 55
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=212,
        name="Scizor",
        types=('Bug', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 130,
            "defense": 100,
            "speed": 65,
            "special": 55
        }),
        moves=('razor wind', 'swords dance', 'cut', 'wing attack')
    ),
    PokemonBase(
        pokedex_number=213,
        name="Shuckle",
        types=('Bug', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 10,
            "defense": 230,
            "speed": 5,
            "special": 10
        }),
        moves=('bind', 'headbutt', 'body slam', 'wrap')
    ),
    PokemonBase(
        pokedex_number=214,
        name="Heracross",
        types=('Bug', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 125,
            "defense": 75,
            "speed": 85,
            "special": 40
        }),
        moves=('swords dance', 'cut', 'headbutt', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=215,
        name="Sneasel",
        types=('Dark', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 95,
            "defense": 55,
            "speed": 115,
            "special": 35
        }),
        moves=('mega punch', 'ice punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=216,
        name="Teddiursa",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 80,
            "defense": 50,
            "speed": 40,
            "special": 50
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=217,
        name="Ursaring",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 130,
            "defense": 75,
            "speed": 55,
            "special": 75
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=218,
        name="Slugma",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 40,
            "speed": 20,
            "special": 70
        }),
        moves=('body slam', 'take down', 'double edge', 'ember')
    ),
    PokemonBase(
        pokedex_number=219,
        name="Magcargo",
        types=('Fire', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 120,
            "speed": 30,
            "special": 90
        }),
        moves=('body slam', 'take down', 'double edge', 'ember')
    ),
    PokemonBase(
        pokedex_number=220,
        name="Swinub",
        types=('Ice', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 40,
            "speed": 50,
            "special": 30
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=221,
        name="Piloswine",
        types=('Ice', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 80,
            "speed": 50,
            "special": 60
        }),
        moves=('headbutt', 'horn attack', 'fury attack', 'tackle')
    ),
    PokemonBase(
        pokedex_number=222,
        name="Corsola",
        types=('Water', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 55,
            "defense": 95,
            "speed": 35,
            "special": 65
        }),
        moves=('headbutt', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=223,
        name="Remoraid",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 65,
            "defense": 35,
            "speed": 65,
            "special": 65
        }),
        moves=('double edge', 'supersonic', 'flamethrower', 'water gun')
    ),
    PokemonBase(
        pokedex_number=224,
        name="Octillery",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 105,
            "defense": 75,
            "speed": 45,
            "special": 105
        }),
        moves=('bind', 'wrap', 'double edge', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=225,
        name="Delibird",
        types=('Ice', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 55,
            "defense": 45,
            "speed": 75,
            "special": 65
        }),
        moves=('mega punch', 'ice punch', 'fly', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=226,
        name="Mantine",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 40,
            "defense": 70,
            "speed": 70,
            "special": 80
        }),
        moves=('wing attack', 'slam', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=227,
        name="Skarmory",
        types=('Steel', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 80,
            "defense": 140,
            "speed": 70,
            "special": 40
        }),
        moves=('swords dance', 'cut', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=228,
        name="Houndour",
        types=('Dark', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 60,
            "defense": 30,
            "speed": 65,
            "special": 80
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=229,
        name="Houndoom",
        types=('Dark', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 90,
            "defense": 50,
            "speed": 95,
            "special": 110
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=230,
        name="Kingdra",
        types=('Water', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 95,
            "defense": 95,
            "speed": 85,
            "special": 95
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=231,
        name="Phanpy",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 60,
            "defense": 60,
            "speed": 40,
            "special": 40
        }),
        moves=('slam', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=232,
        name="Donphan",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 120,
            "defense": 120,
            "speed": 50,
            "special": 60
        }),
        moves=('slam', 'headbutt', 'horn attack', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=233,
        name="Porygon2",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 80,
            "defense": 90,
            "speed": 60,
            "special": 105
        }),
        moves=('tackle', 'take down', 'double edge', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=234,
        name="Stantler",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 73,
            "attack": 95,
            "defense": 62,
            "speed": 85,
            "special": 85
        }),
        moves=('stomp', 'double kick', 'jump kick', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=235,
        name="Smeargle",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 20,
            "defense": 35,
            "speed": 75,
            "special": 20
        }),
        moves=('sketch',)
    ),
    PokemonBase(
        pokedex_number=236,
        name="Tyrogue",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 35,
            "defense": 35,
            "speed": 35,
            "special": 35
        }),
        moves=('mega punch', 'mega kick', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=237,
        name="Hitmontop",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 95,
            "defense": 95,
            "speed": 70,
            "special": 35
        }),
        moves=('mega punch', 'mega kick', 'rolling kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=238,
        name="Smoochum",
        types=('Ice', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 15,
            "speed": 65,
            "special": 85
        }),
        moves=('pound', 'mega punch', 'ice punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=239,
        name="Elekid",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 63,
            "defense": 37,
            "speed": 95,
            "special": 65
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=240,
        name="Magby",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 75,
            "defense": 37,
            "speed": 83,
            "special": 70
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=241,
        name="Miltank",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 80,
            "defense": 105,
            "speed": 100,
            "special": 40
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=242,
        name="Blissey",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 255,
            "attack": 10,
            "defense": 10,
            "speed": 55,
            "special": 75
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=243,
        name="Raikou",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 85,
            "defense": 75,
            "speed": 115,
            "special": 115
        }),
        moves=('cut', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=244,
        name="Entei",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 115,
            "defense": 85,
            "speed": 100,
            "special": 90
        }),
        moves=('cut', 'stomp', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=245,
        name="Suicune",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 75,
            "defense": 115,
            "speed": 85,
            "special": 90
        }),
        moves=('cut', 'gust', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=246,
        name="Larvitar",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 64,
            "defense": 50,
            "speed": 41,
            "special": 45
        }),
        moves=('stomp', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=247,
        name="Pupitar",
        types=('Rock', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 84,
            "defense": 70,
            "speed": 51,
            "special": 65
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=248,
        name="Tyranitar",
        types=('Rock', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 134,
            "defense": 110,
            "speed": 61,
            "special": 95
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=249,
        name="Lugia",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 106,
            "attack": 90,
            "defense": 130,
            "speed": 110,
            "special": 90
        }),
        moves=('gust', 'whirlwind', 'fly', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=250,
        name="Ho-oh",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 106,
            "attack": 130,
            "defense": 90,
            "speed": 90,
            "special": 110
        }),
        moves=('gust', 'whirlwind', 'fly', 'body slam')
    ),
    PokemonBase(
        pokedex_number=251,
        name="Celebi",
        types=('Psychic', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('swords dance', 'cut', 'double edge', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=252,
        name="Treecko",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 35,
            "speed": 70,
            "special": 65
        }),
        moves=('pound', 'mega punch', 'thunder punch', 'razor wind')
    ),
    PokemonBase(
        pokedex_number=253,
        name="Grovyle",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 45,
            "speed": 95,
            "special": 85
        }),
        moves=('pound', 'mega punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=254,
        name="Sceptile",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 65,
            "speed": 120,
            "special": 105
        }),
        moves=('pound', 'mega punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=255,
        name="Torchic",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 60,
            "defense": 40,
            "speed": 45,
            "special": 70
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=256,
        name="Combusken",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 60,
            "speed": 55,
            "special": 85
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=257,
        name="Blaziken",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 70,
            "speed": 80,
            "special": 110
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=258,
        name="Mudkip",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 70,
            "defense": 50,
            "speed": 40,
            "special": 50
        }),
        moves=('stomp', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=259,
        name="Marshtomp",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 70,
            "speed": 50,
            "special": 60
        }),
        moves=('mega punch', 'ice punch', 'stomp', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=260,
        name="Swampert",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 110,
            "defense": 90,
            "speed": 60,
            "special": 85
        }),
        moves=('mega punch', 'ice punch', 'stomp', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=261,
        name="Poochyena",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 55,
            "defense": 35,
            "speed": 35,
            "special": 30
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=262,
        name="Mightyena",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 90,
            "defense": 70,
            "speed": 70,
            "special": 60
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=263,
        name="Zigzagoon",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 30,
            "defense": 41,
            "speed": 60,
            "special": 30
        }),
        moves=('cut', 'sand attack', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=264,
        name="Linoone",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 70,
            "defense": 61,
            "speed": 100,
            "special": 50
        }),
        moves=('cut', 'sand attack', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=265,
        name="Wurmple",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 45,
            "defense": 35,
            "speed": 20,
            "special": 20
        }),
        moves=('tackle', 'poison sting', 'string shot', 'snore')
    ),
    PokemonBase(
        pokedex_number=266,
        name="Silcoon",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 35,
            "defense": 55,
            "speed": 15,
            "special": 25
        }),
        moves=('tackle', 'poison sting', 'string shot', 'harden')
    ),
    PokemonBase(
        pokedex_number=267,
        name="Beautifly",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 70,
            "defense": 50,
            "speed": 65,
            "special": 100
        }),
        moves=('gust', 'whirlwind', 'tackle', 'double edge')
    ),
    PokemonBase(
        pokedex_number=268,
        name="Cascoon",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 35,
            "defense": 55,
            "speed": 15,
            "special": 25
        }),
        moves=('tackle', 'poison sting', 'string shot', 'harden')
    ),
    PokemonBase(
        pokedex_number=269,
        name="Dustox",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 70,
            "speed": 65,
            "special": 50
        }),
        moves=('gust', 'whirlwind', 'tackle', 'double edge')
    ),
    PokemonBase(
        pokedex_number=270,
        name="Lotad",
        types=('Water', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 30,
            "speed": 30,
            "special": 40
        }),
        moves=('swords dance', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=271,
        name="Lombre",
        types=('Water', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 50,
            "speed": 50,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=272,
        name="Ludicolo",
        types=('Water', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 70,
            "defense": 70,
            "speed": 70,
            "special": 90
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=273,
        name="Seedot",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 50,
            "speed": 30,
            "special": 30
        }),
        moves=('razor wind', 'swords dance', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=274,
        name="Nuzleaf",
        types=('Grass', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 70,
            "defense": 40,
            "speed": 60,
            "special": 60
        }),
        moves=('pound', 'razor wind', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=275,
        name="Shiftry",
        types=('Grass', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 100,
            "defense": 60,
            "speed": 80,
            "special": 90
        }),
        moves=('pound', 'swords dance', 'cut', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=276,
        name="Taillow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 30,
            "speed": 85,
            "special": 30
        }),
        moves=('wing attack', 'whirlwind', 'fly', 'double edge')
    ),
    PokemonBase(
        pokedex_number=277,
        name="Swellow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 60,
            "speed": 125,
            "special": 75
        }),
        moves=('wing attack', 'fly', 'double edge', 'growl')
    ),
    PokemonBase(
        pokedex_number=278,
        name="Wingull",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 30,
            "speed": 85,
            "special": 55
        }),
        moves=('gust', 'wing attack', 'fly', 'take down')
    ),
    PokemonBase(
        pokedex_number=279,
        name="Pelipper",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 100,
            "speed": 65,
            "special": 95
        }),
        moves=('wing attack', 'fly', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=280,
        name="Ralts",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 28,
            "attack": 25,
            "defense": 25,
            "speed": 40,
            "special": 45
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=281,
        name="Kirlia",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 35,
            "defense": 35,
            "speed": 50,
            "special": 65
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=282,
        name="Gardevoir",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 65,
            "defense": 65,
            "speed": 80,
            "special": 125
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=283,
        name="Surskit",
        types=('Bug', 'Water'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 32,
            "speed": 65,
            "special": 50
        }),
        moves=('take down', 'double edge', 'mist', 'water gun')
    ),
    PokemonBase(
        pokedex_number=284,
        name="Masquerain",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 60,
            "defense": 62,
            "speed": 80,
            "special": 100
        }),
        moves=('gust', 'whirlwind', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=285,
        name="Shroomish",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 40,
            "defense": 60,
            "speed": 35,
            "special": 40
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=286,
        name="Breloom",
        types=('Grass', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 130,
            "defense": 80,
            "speed": 70,
            "special": 60
        }),
        moves=('mega punch', 'thunder punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=287,
        name="Slakoth",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 60,
            "speed": 30,
            "special": 35
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=288,
        name="Vigoroth",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 80,
            "speed": 90,
            "special": 55
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=289,
        name="Slaking",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 150,
            "attack": 160,
            "defense": 100,
            "speed": 100,
            "special": 95
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=290,
        name="Nincada",
        types=('Bug', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 31,
            "attack": 45,
            "defense": 90,
            "speed": 40,
            "special": 30
        }),
        moves=('scratch', 'cut', 'gust', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=291,
        name="Ninjask",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 90,
            "defense": 45,
            "speed": 160,
            "special": 50
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=292,
        name="Shedinja",
        types=('Bug', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 1,
            "attack": 90,
            "defense": 45,
            "speed": 40,
            "special": 30
        }),
        moves=('scratch', 'cut', 'sand attack', 'double edge')
    ),
    PokemonBase(
        pokedex_number=293,
        name="Whismur",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 64,
            "attack": 51,
            "defense": 23,
            "speed": 28,
            "special": 51
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=294,
        name="Loudred",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 84,
            "attack": 71,
            "defense": 43,
            "speed": 48,
            "special": 71
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=295,
        name="Exploud",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 104,
            "attack": 91,
            "defense": 63,
            "speed": 68,
            "special": 91
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=296,
        name="Makuhita",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 60,
            "defense": 30,
            "speed": 25,
            "special": 20
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=297,
        name="Hariyama",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 144,
            "attack": 120,
            "defense": 60,
            "speed": 50,
            "special": 40
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=298,
        name="Azurill",
        types=('Normal', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 20,
            "defense": 40,
            "speed": 20,
            "special": 20
        }),
        moves=('slam', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=299,
        name="Nosepass",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 45,
            "defense": 135,
            "speed": 30,
            "special": 45
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=300,
        name="Skitty",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 45,
            "defense": 45,
            "speed": 50,
            "special": 35
        }),
        moves=('double slap', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=301,
        name="Delcatty",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 65,
            "defense": 65,
            "speed": 90,
            "special": 55
        }),
        moves=('double slap', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=302,
        name="Sableye",
        types=('Dark', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 75,
            "defense": 75,
            "speed": 50,
            "special": 65
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=303,
        name="Mawile",
        types=('Steel', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 85,
            "defense": 85,
            "speed": 50,
            "special": 55
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'vice grip')
    ),
    PokemonBase(
        pokedex_number=304,
        name="Aron",
        types=('Steel', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 70,
            "defense": 100,
            "speed": 30,
            "special": 40
        }),
        moves=('cut', 'stomp', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=305,
        name="Lairon",
        types=('Steel', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 90,
            "defense": 140,
            "speed": 40,
            "special": 50
        }),
        moves=('cut', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=306,
        name="Aggron",
        types=('Steel', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 110,
            "defense": 180,
            "speed": 50,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=307,
        name="Meditite",
        types=('Fighting', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 40,
            "defense": 55,
            "speed": 60,
            "special": 40
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=308,
        name="Medicham",
        types=('Fighting', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 75,
            "speed": 80,
            "special": 60
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=309,
        name="Electrike",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 40,
            "speed": 65,
            "special": 65
        }),
        moves=('headbutt', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=310,
        name="Manectric",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 75,
            "defense": 60,
            "speed": 105,
            "special": 105
        }),
        moves=('headbutt', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=311,
        name="Plusle",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 40,
            "speed": 95,
            "special": 85
        }),
        moves=('mega punch', 'thunder punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=312,
        name="Minun",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 40,
            "defense": 50,
            "speed": 95,
            "special": 75
        }),
        moves=('mega punch', 'thunder punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=313,
        name="Volbeat",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 73,
            "defense": 75,
            "speed": 85,
            "special": 47
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=314,
        name="Illumise",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 47,
            "defense": 75,
            "speed": 85,
            "special": 73
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=315,
        name="Roselia",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 60,
            "defense": 45,
            "speed": 65,
            "special": 100
        }),
        moves=('swords dance', 'cut', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=316,
        name="Gulpin",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 43,
            "defense": 53,
            "speed": 40,
            "special": 43
        }),
        moves=('pound', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=317,
        name="Swalot",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 73,
            "defense": 83,
            "speed": 55,
            "special": 73
        }),
        moves=('pound', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=318,
        name="Carvanha",
        types=('Water', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 90,
            "defense": 20,
            "speed": 65,
            "special": 65
        }),
        moves=('take down', 'thrash', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=319,
        name="Sharpedo",
        types=('Water', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 120,
            "defense": 40,
            "speed": 95,
            "special": 95
        }),
        moves=('take down', 'double edge', 'leer', 'bite')
    ),
    PokemonBase(
        pokedex_number=320,
        name="Wailmer",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 130,
            "attack": 70,
            "defense": 35,
            "speed": 60,
            "special": 70
        }),
        moves=('headbutt', 'body slam', 'thrash', 'double edge')
    ),
    PokemonBase(
        pokedex_number=321,
        name="Wailord",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 170,
            "attack": 90,
            "defense": 45,
            "speed": 60,
            "special": 90
        }),
        moves=('headbutt', 'body slam', 'double edge', 'growl')
    ),
    PokemonBase(
        pokedex_number=322,
        name="Numel",
        types=('Fire', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 40,
            "speed": 35,
            "special": 65
        }),
        moves=('stomp', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=323,
        name="Camerupt",
        types=('Fire', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 100,
            "defense": 70,
            "speed": 40,
            "special": 105
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=324,
        name="Torkoal",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 140,
            "speed": 20,
            "special": 85
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=325,
        name="Spoink",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 25,
            "defense": 35,
            "speed": 60,
            "special": 70
        }),
        moves=('whirlwind', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=326,
        name="Grumpig",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 45,
            "defense": 65,
            "speed": 80,
            "special": 90
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=327,
        name="Spinda",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 60,
            "speed": 60,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=328,
        name="Trapinch",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 100,
            "defense": 45,
            "speed": 10,
            "special": 45
        }),
        moves=('gust', 'sand attack', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=329,
        name="Vibrava",
        types=('Ground', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 70,
            "defense": 50,
            "speed": 70,
            "special": 50
        }),
        moves=('gust', 'fly', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=330,
        name="Flygon",
        types=('Ground', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 100,
            "defense": 80,
            "speed": 100,
            "special": 80
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'gust')
    ),
    PokemonBase(
        pokedex_number=331,
        name="Cacnea",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 85,
            "defense": 40,
            "speed": 35,
            "special": 85
        }),
        moves=('mega punch', 'thunder punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=332,
        name="Cacturne",
        types=('Grass', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 115,
            "defense": 60,
            "speed": 55,
            "special": 115
        }),
        moves=('mega punch', 'thunder punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=333,
        name="Swablu",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 40,
            "defense": 60,
            "speed": 50,
            "special": 40
        }),
        moves=('fly', 'fury attack', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=334,
        name="Altaria",
        types=('Dragon', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 70,
            "defense": 90,
            "speed": 80,
            "special": 70
        }),
        moves=('fly', 'fury attack', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=335,
        name="Zangoose",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 73,
            "attack": 115,
            "defense": 60,
            "speed": 90,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=336,
        name="Seviper",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 73,
            "attack": 100,
            "defense": 60,
            "speed": 65,
            "special": 100
        }),
        moves=('swords dance', 'bind', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=337,
        name="Lunatone",
        types=('Rock', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 55,
            "defense": 65,
            "speed": 70,
            "special": 95
        }),
        moves=('tackle', 'body slam', 'double edge', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=338,
        name="Solrock",
        types=('Rock', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 95,
            "defense": 85,
            "speed": 70,
            "special": 55
        }),
        moves=('swords dance', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=339,
        name="Barboach",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 48,
            "defense": 43,
            "speed": 60,
            "special": 46
        }),
        moves=('headbutt', 'take down', 'thrash', 'double edge')
    ),
    PokemonBase(
        pokedex_number=340,
        name="Whiscash",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 78,
            "defense": 73,
            "speed": 60,
            "special": 76
        }),
        moves=('headbutt', 'body slam', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=341,
        name="Corphish",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 43,
            "attack": 80,
            "defense": 65,
            "speed": 35,
            "special": 50
        }),
        moves=('vice grip', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=342,
        name="Crawdaunt",
        types=('Water', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 63,
            "attack": 120,
            "defense": 85,
            "speed": 55,
            "special": 90
        }),
        moves=('vice grip', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=343,
        name="Baltoy",
        types=('Ground', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 55,
            "speed": 55,
            "special": 40
        }),
        moves=('headbutt', 'double edge', 'ice beam', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=344,
        name="Claydol",
        types=('Ground', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 70,
            "defense": 105,
            "speed": 75,
            "special": 70
        }),
        moves=('headbutt', 'double edge', 'ice beam', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=345,
        name="Lileep",
        types=('Rock', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 66,
            "attack": 41,
            "defense": 77,
            "speed": 23,
            "special": 61
        }),
        moves=('swords dance', 'bind', 'body slam', 'wrap')
    ),
    PokemonBase(
        pokedex_number=346,
        name="Cradily",
        types=('Rock', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 86,
            "attack": 81,
            "defense": 97,
            "speed": 43,
            "special": 81
        }),
        moves=('swords dance', 'bind', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=347,
        name="Anorith",
        types=('Rock', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 95,
            "defense": 50,
            "speed": 75,
            "special": 40
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=348,
        name="Armaldo",
        types=('Rock', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 125,
            "defense": 100,
            "speed": 45,
            "special": 70
        }),
        moves=('scratch', 'swords dance', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=349,
        name="Feebas",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 15,
            "defense": 20,
            "speed": 80,
            "special": 10
        }),
        moves=('tackle', 'double edge', 'mist', 'surf')
    ),
    PokemonBase(
        pokedex_number=350,
        name="Milotic",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 60,
            "defense": 79,
            "speed": 81,
            "special": 100
        }),
        moves=('bind', 'tackle', 'body slam', 'wrap')
    ),
    PokemonBase(
        pokedex_number=351,
        name="Castform",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 70,
            "defense": 70,
            "speed": 70,
            "special": 70
        }),
        moves=('headbutt', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=352,
        name="Kecleon",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 90,
            "defense": 70,
            "speed": 40,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=353,
        name="Shuppet",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 75,
            "defense": 35,
            "speed": 45,
            "special": 63
        }),
        moves=('headbutt', 'body slam', 'double edge', 'disable')
    ),
    PokemonBase(
        pokedex_number=354,
        name="Banette",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 64,
            "attack": 115,
            "defense": 65,
            "speed": 65,
            "special": 83
        }),
        moves=('swords dance', 'headbutt', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=355,
        name="Duskull",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 40,
            "defense": 90,
            "speed": 25,
            "special": 30
        }),
        moves=('headbutt', 'body slam', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=356,
        name="Dusclops",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 70,
            "defense": 130,
            "speed": 25,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=357,
        name="Tropius",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 99,
            "attack": 68,
            "defense": 83,
            "speed": 51,
            "special": 72
        }),
        moves=('razor wind', 'swords dance', 'cut', 'gust')
    ),
    PokemonBase(
        pokedex_number=358,
        name="Chimecho",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 50,
            "defense": 80,
            "speed": 65,
            "special": 95
        }),
        moves=('bind', 'tackle', 'wrap', 'take down')
    ),
    PokemonBase(
        pokedex_number=359,
        name="Absol",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 130,
            "defense": 60,
            "speed": 75,
            "special": 75
        }),
        moves=('scratch', 'razor wind', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=360,
        name="Wynaut",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 23,
            "defense": 48,
            "speed": 23,
            "special": 23
        }),
        moves=('counter', 'amnesia', 'splash', 'destiny bond')
    ),
    PokemonBase(
        pokedex_number=361,
        name="Snorunt",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 50,
            "speed": 50,
            "special": 50
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=362,
        name="Glalie",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 80,
            "speed": 80,
            "special": 80
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=363,
        name="Spheal",
        types=('Ice', 'Water'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 40,
            "defense": 50,
            "speed": 25,
            "special": 55
        }),
        moves=('headbutt', 'body slam', 'double edge', 'growl')
    ),
    PokemonBase(
        pokedex_number=364,
        name="Sealeo",
        types=('Ice', 'Water'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 60,
            "defense": 70,
            "speed": 45,
            "special": 75
        }),
        moves=('headbutt', 'body slam', 'double edge', 'growl')
    ),
    PokemonBase(
        pokedex_number=365,
        name="Walrein",
        types=('Ice', 'Water'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 80,
            "defense": 90,
            "speed": 65,
            "special": 95
        }),
        moves=('swords dance', 'headbutt', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=366,
        name="Clamperl",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 64,
            "defense": 85,
            "speed": 32,
            "special": 74
        }),
        moves=('body slam', 'double edge', 'supersonic', 'water gun')
    ),
    PokemonBase(
        pokedex_number=367,
        name="Huntail",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 104,
            "defense": 105,
            "speed": 52,
            "special": 94
        }),
        moves=('bind', 'body slam', 'double edge', 'bite')
    ),
    PokemonBase(
        pokedex_number=368,
        name="Gorebyss",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 84,
            "defense": 105,
            "speed": 52,
            "special": 114
        }),
        moves=('bind', 'body slam', 'double edge', 'water gun')
    ),
    PokemonBase(
        pokedex_number=369,
        name="Relicanth",
        types=('Water', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 90,
            "defense": 130,
            "speed": 55,
            "special": 45
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=370,
        name="Luvdisc",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 43,
            "attack": 30,
            "defense": 55,
            "speed": 97,
            "special": 40
        }),
        moves=('tackle', 'take down', 'double edge', 'supersonic')
    ),
    PokemonBase(
        pokedex_number=371,
        name="Bagon",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 75,
            "defense": 60,
            "speed": 50,
            "special": 40
        }),
        moves=('cut', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=372,
        name="Shelgon",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 95,
            "defense": 100,
            "speed": 50,
            "special": 60
        }),
        moves=('cut', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=373,
        name="Salamence",
        types=('Dragon', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 135,
            "defense": 80,
            "speed": 100,
            "special": 110
        }),
        moves=('cut', 'fly', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=374,
        name="Beldum",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 80,
            "speed": 30,
            "special": 35
        }),
        moves=('headbutt', 'tackle', 'take down', 'iron defense')
    ),
    PokemonBase(
        pokedex_number=375,
        name="Metang",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 75,
            "defense": 100,
            "speed": 50,
            "special": 55
        }),
        moves=('ice punch', 'thunder punch', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=376,
        name="Metagross",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 135,
            "defense": 130,
            "speed": 70,
            "special": 95
        }),
        moves=('ice punch', 'thunder punch', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=377,
        name="Regirock",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 100,
            "defense": 200,
            "speed": 50,
            "special": 50
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=378,
        name="Regice",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 50,
            "defense": 100,
            "speed": 50,
            "special": 100
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'stomp')
    ),
    PokemonBase(
        pokedex_number=379,
        name="Registeel",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 75,
            "defense": 150,
            "speed": 50,
            "special": 75
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'stomp')
    ),
    PokemonBase(
        pokedex_number=380,
        name="Latias",
        types=('Dragon', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 90,
            "speed": 110,
            "special": 110
        }),
        moves=('cut', 'fly', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=381,
        name="Latios",
        types=('Dragon', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 90,
            "defense": 80,
            "speed": 110,
            "special": 130
        }),
        moves=('cut', 'fly', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=382,
        name="Kyogre",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 90,
            "speed": 90,
            "special": 150
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=383,
        name="Groudon",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 150,
            "defense": 140,
            "speed": 90,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=384,
        name="Rayquaza",
        types=('Dragon', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 150,
            "defense": 90,
            "speed": 95,
            "special": 150
        }),
        moves=('swords dance', 'fly', 'bind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=385,
        name="Jirachi",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=386,
        name="Deoxys-normal",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 150,
            "defense": 50,
            "speed": 150,
            "special": 150
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'cut')
    ),
    PokemonBase(
        pokedex_number=387,
        name="Turtwig",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 68,
            "defense": 64,
            "speed": 31,
            "special": 45
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=388,
        name="Grotle",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 89,
            "defense": 85,
            "speed": 36,
            "special": 55
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=389,
        name="Torterra",
        types=('Grass', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 109,
            "defense": 105,
            "speed": 56,
            "special": 75
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=390,
        name="Chimchar",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 58,
            "defense": 44,
            "speed": 61,
            "special": 58
        }),
        moves=('fire punch', 'thunder punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=391,
        name="Monferno",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 64,
            "attack": 78,
            "defense": 52,
            "speed": 81,
            "special": 78
        }),
        moves=('fire punch', 'thunder punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=392,
        name="Infernape",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 104,
            "defense": 71,
            "speed": 108,
            "special": 104
        }),
        moves=('fire punch', 'thunder punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=393,
        name="Piplup",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 53,
            "attack": 51,
            "defense": 53,
            "speed": 40,
            "special": 61
        }),
        moves=('pound', 'cut', 'headbutt', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=394,
        name="Prinplup",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 64,
            "attack": 66,
            "defense": 68,
            "speed": 50,
            "special": 81
        }),
        moves=('pound', 'cut', 'headbutt', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=395,
        name="Empoleon",
        types=('Water', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 84,
            "attack": 86,
            "defense": 88,
            "speed": 60,
            "special": 111
        }),
        moves=('pound', 'swords dance', 'cut', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=396,
        name="Starly",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 30,
            "speed": 60,
            "special": 30
        }),
        moves=('gust', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=397,
        name="Staravia",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 75,
            "defense": 50,
            "speed": 80,
            "special": 40
        }),
        moves=('gust', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=398,
        name="Staraptor",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 120,
            "defense": 70,
            "speed": 100,
            "special": 50
        }),
        moves=('gust', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=399,
        name="Bidoof",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 45,
            "defense": 40,
            "speed": 31,
            "special": 35
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=400,
        name="Bibarel",
        types=('Normal', 'Water'),
        base_stats=MappingProxyType({
            "hp": 79,
            "attack": 85,
            "defense": 60,
            "speed": 71,
            "special": 55
        }),
        moves=('swords dance', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=401,
        name="Kricketot",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 37,
            "attack": 25,
            "defense": 41,
            "speed": 25,
            "special": 25
        }),
        moves=('pound', 'tackle', 'growl', 'absorb')
    ),
    PokemonBase(
        pokedex_number=402,
        name="Kricketune",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 77,
            "attack": 85,
            "defense": 51,
            "speed": 65,
            "special": 55
        }),
        moves=('pound', 'swords dance', 'cut', 'tackle')
    ),
    PokemonBase(
        pokedex_number=403,
        name="Shinx",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 65,
            "defense": 34,
            "speed": 45,
            "special": 40
        }),
        moves=('double kick', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=404,
        name="Luxio",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 49,
            "speed": 60,
            "special": 60
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=405,
        name="Luxray",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 79,
            "speed": 70,
            "special": 95
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=406,
        name="Budew",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 35,
            "speed": 55,
            "special": 50
        }),
        moves=('swords dance', 'cut', 'poison sting', 'pin missile')
    ),
    PokemonBase(
        pokedex_number=407,
        name="Roserade",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 70,
            "defense": 65,
            "speed": 90,
            "special": 125
        }),
        moves=('swords dance', 'cut', 'body slam', 'poison sting')
    ),
    PokemonBase(
        pokedex_number=408,
        name="Cranidos",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 125,
            "defense": 40,
            "speed": 58,
            "special": 30
        }),
        moves=('fire punch', 'thunder punch', 'swords dance', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=409,
        name="Rampardos",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 97,
            "attack": 165,
            "defense": 60,
            "speed": 58,
            "special": 65
        }),
        moves=('fire punch', 'thunder punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=410,
        name="Shieldon",
        types=('Rock', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 42,
            "defense": 118,
            "speed": 30,
            "special": 42
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=411,
        name="Bastiodon",
        types=('Rock', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 52,
            "defense": 168,
            "speed": 30,
            "special": 47
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=412,
        name="Burmy",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 29,
            "defense": 45,
            "speed": 36,
            "special": 29
        }),
        moves=('tackle', 'string shot', 'snore', 'protect')
    ),
    PokemonBase(
        pokedex_number=413,
        name="Wormadam-plant",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 59,
            "defense": 85,
            "speed": 36,
            "special": 79
        }),
        moves=('gust', 'tackle', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=414,
        name="Mothim",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 94,
            "defense": 50,
            "speed": 66,
            "special": 94
        }),
        moves=('gust', 'tackle', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=415,
        name="Combee",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 30,
            "defense": 42,
            "speed": 70,
            "special": 30
        }),
        moves=('gust', 'string shot', 'swift', 'snore')
    ),
    PokemonBase(
        pokedex_number=416,
        name="Vespiquen",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 80,
            "defense": 102,
            "speed": 40,
            "special": 80
        }),
        moves=('cut', 'gust', 'take down', 'poison sting')
    ),
    PokemonBase(
        pokedex_number=417,
        name="Pachirisu",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 70,
            "speed": 95,
            "special": 45
        }),
        moves=('thunder punch', 'cut', 'headbutt', 'take down')
    ),
    PokemonBase(
        pokedex_number=418,
        name="Buizel",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 65,
            "defense": 35,
            "speed": 85,
            "special": 60
        }),
        moves=('double slap', 'ice punch', 'razor wind', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=419,
        name="Floatzel",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 105,
            "defense": 55,
            "speed": 115,
            "special": 85
        }),
        moves=('ice punch', 'razor wind', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=420,
        name="Cherubi",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 35,
            "defense": 45,
            "speed": 35,
            "special": 62
        }),
        moves=('swords dance', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=421,
        name="Cherrim",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 60,
            "defense": 70,
            "speed": 85,
            "special": 87
        }),
        moves=('swords dance', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=422,
        name="Shellos",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 48,
            "defense": 48,
            "speed": 34,
            "special": 57
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=423,
        name="Gastrodon",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 111,
            "attack": 83,
            "defense": 68,
            "speed": 39,
            "special": 92
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=424,
        name="Ambipom",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 100,
            "defense": 66,
            "speed": 115,
            "special": 60
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=425,
        name="Drifloon",
        types=('Ghost', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 50,
            "defense": 34,
            "speed": 70,
            "special": 60
        }),
        moves=('cut', 'gust', 'fly', 'bind')
    ),
    PokemonBase(
        pokedex_number=426,
        name="Drifblim",
        types=('Ghost', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 150,
            "attack": 80,
            "defense": 44,
            "speed": 80,
            "special": 90
        }),
        moves=('cut', 'gust', 'fly', 'bind')
    ),
    PokemonBase(
        pokedex_number=427,
        name="Buneary",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 66,
            "defense": 44,
            "speed": 85,
            "special": 44
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=428,
        name="Lopunny",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 76,
            "defense": 84,
            "speed": 105,
            "special": 54
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=429,
        name="Mismagius",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 60,
            "speed": 105,
            "special": 105
        }),
        moves=('headbutt', 'growl', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=430,
        name="Honchkrow",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 125,
            "defense": 52,
            "speed": 71,
            "special": 105
        }),
        moves=('gust', 'wing attack', 'fly', 'take down')
    ),
    PokemonBase(
        pokedex_number=431,
        name="Glameow",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 49,
            "attack": 55,
            "defense": 42,
            "speed": 85,
            "special": 42
        }),
        moves=('scratch', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=432,
        name="Purugly",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 82,
            "defense": 64,
            "speed": 112,
            "special": 64
        }),
        moves=('scratch', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=433,
        name="Chingling",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 50,
            "speed": 45,
            "special": 65
        }),
        moves=('bind', 'tackle', 'wrap', 'double edge')
    ),
    PokemonBase(
        pokedex_number=434,
        name="Stunky",
        types=('Poison', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 63,
            "attack": 63,
            "defense": 47,
            "speed": 74,
            "special": 41
        }),
        moves=('scratch', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=435,
        name="Skuntank",
        types=('Poison', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 103,
            "attack": 93,
            "defense": 67,
            "speed": 84,
            "special": 71
        }),
        moves=('scratch', 'cut', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=436,
        name="Bronzor",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 24,
            "defense": 86,
            "speed": 23,
            "special": 24
        }),
        moves=('tackle', 'body slam', 'take down', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=437,
        name="Bronzong",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 89,
            "defense": 116,
            "speed": 33,
            "special": 79
        }),
        moves=('tackle', 'body slam', 'take down', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=438,
        name="Bonsly",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 80,
            "defense": 95,
            "speed": 10,
            "special": 10
        }),
        moves=('slam', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=439,
        name="Mime-jr",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 20,
            "attack": 25,
            "defense": 45,
            "speed": 60,
            "special": 70
        }),
        moves=('pound', 'double slap', 'headbutt', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=440,
        name="Happiny",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 5,
            "defense": 5,
            "speed": 30,
            "special": 15
        }),
        moves=('pound', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=441,
        name="Chatot",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 65,
            "defense": 45,
            "speed": 91,
            "special": 92
        }),
        moves=('gust', 'fly', 'fury attack', 'growl')
    ),
    PokemonBase(
        pokedex_number=442,
        name="Spiritomb",
        types=('Ghost', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 92,
            "defense": 108,
            "speed": 35,
            "special": 92
        }),
        moves=('body slam', 'disable', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=443,
        name="Gible",
        types=('Dragon', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 70,
            "defense": 45,
            "speed": 42,
            "special": 40
        }),
        moves=('swords dance', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=444,
        name="Gabite",
        types=('Dragon', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 90,
            "defense": 65,
            "speed": 82,
            "special": 50
        }),
        moves=('swords dance', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=445,
        name="Garchomp",
        types=('Dragon', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 108,
            "attack": 130,
            "defense": 95,
            "speed": 102,
            "special": 80
        }),
        moves=('swords dance', 'cut', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=446,
        name="Munchlax",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 135,
            "attack": 85,
            "defense": 40,
            "speed": 5,
            "special": 40
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=447,
        name="Riolu",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 70,
            "defense": 40,
            "speed": 60,
            "special": 35
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=448,
        name="Lucario",
        types=('Fighting', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 110,
            "defense": 70,
            "speed": 90,
            "special": 115
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=449,
        name="Hippopotas",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 72,
            "defense": 78,
            "speed": 32,
            "special": 38
        }),
        moves=('whirlwind', 'sand attack', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=450,
        name="Hippowdon",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 108,
            "attack": 112,
            "defense": 118,
            "speed": 47,
            "special": 68
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=451,
        name="Skorupi",
        types=('Poison', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 50,
            "defense": 90,
            "speed": 65,
            "special": 30
        }),
        moves=('swords dance', 'cut', 'whirlwind', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=452,
        name="Drapion",
        types=('Poison', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 90,
            "defense": 110,
            "speed": 95,
            "special": 60
        }),
        moves=('swords dance', 'cut', 'headbutt', 'poison sting')
    ),
    PokemonBase(
        pokedex_number=453,
        name="Croagunk",
        types=('Poison', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 61,
            "defense": 40,
            "speed": 50,
            "special": 61
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=454,
        name="Toxicroak",
        types=('Poison', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 83,
            "attack": 106,
            "defense": 65,
            "speed": 85,
            "special": 86
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=455,
        name="Carnivine",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 100,
            "defense": 72,
            "speed": 46,
            "special": 90
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=456,
        name="Finneon",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 49,
            "attack": 49,
            "defense": 56,
            "speed": 66,
            "special": 49
        }),
        moves=('pound', 'gust', 'take down', 'water gun')
    ),
    PokemonBase(
        pokedex_number=457,
        name="Lumineon",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 69,
            "attack": 69,
            "defense": 76,
            "speed": 91,
            "special": 69
        }),
        moves=('pound', 'gust', 'take down', 'water gun')
    ),
    PokemonBase(
        pokedex_number=458,
        name="Mantyke",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 20,
            "defense": 50,
            "speed": 50,
            "special": 60
        }),
        moves=('wing attack', 'slam', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=459,
        name="Snover",
        types=('Grass', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 62,
            "defense": 50,
            "speed": 40,
            "special": 62
        }),
        moves=('mega punch', 'ice punch', 'swords dance', 'stomp')
    ),
    PokemonBase(
        pokedex_number=460,
        name="Abomasnow",
        types=('Grass', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 92,
            "defense": 75,
            "speed": 60,
            "special": 92
        }),
        moves=('mega punch', 'ice punch', 'swords dance', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=461,
        name="Weavile",
        types=('Dark', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 120,
            "defense": 65,
            "speed": 125,
            "special": 45
        }),
        moves=('mega punch', 'ice punch', 'scratch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=462,
        name="Magnezone",
        types=('Electric', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 70,
            "defense": 115,
            "speed": 60,
            "special": 130
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=463,
        name="Lickilicky",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 85,
            "defense": 95,
            "speed": 50,
            "special": 80
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=464,
        name="Rhyperior",
        types=('Ground', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 140,
            "defense": 130,
            "speed": 40,
            "special": 55
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=465,
        name="Tangrowth",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 125,
            "speed": 50,
            "special": 110
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=466,
        name="Electivire",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 123,
            "defense": 67,
            "speed": 95,
            "special": 95
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=467,
        name="Magmortar",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 95,
            "defense": 67,
            "speed": 83,
            "special": 125
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=468,
        name="Togekiss",
        types=('Fairy', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 50,
            "defense": 95,
            "speed": 80,
            "special": 120
        }),
        moves=('pound', 'mega punch', 'fly', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=469,
        name="Yanmega",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 86,
            "attack": 76,
            "defense": 86,
            "speed": 95,
            "special": 116
        }),
        moves=('swords dance', 'gust', 'wing attack', 'whirlwind')
    ),
    PokemonBase(
        pokedex_number=470,
        name="Leafeon",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 110,
            "defense": 130,
            "speed": 95,
            "special": 60
        }),
        moves=('pay day', 'swords dance', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=471,
        name="Glaceon",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 60,
            "defense": 110,
            "speed": 65,
            "special": 130
        }),
        moves=('pay day', 'sand attack', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=472,
        name="Gliscor",
        types=('Ground', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 95,
            "defense": 125,
            "speed": 95,
            "special": 45
        }),
        moves=('guillotine', 'swords dance', 'cut', 'wing attack')
    ),
    PokemonBase(
        pokedex_number=473,
        name="Mamoswine",
        types=('Ice', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 130,
            "defense": 80,
            "speed": 80,
            "special": 70
        }),
        moves=('headbutt', 'fury attack', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=474,
        name="Porygon-z",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 80,
            "defense": 70,
            "speed": 90,
            "special": 135
        }),
        moves=('tackle', 'take down', 'double edge', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=475,
        name="Gallade",
        types=('Psychic', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 125,
            "defense": 65,
            "speed": 80,
            "special": 65
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=476,
        name="Probopass",
        types=('Rock', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 55,
            "defense": 145,
            "speed": 40,
            "special": 75
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=477,
        name="Dusknoir",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 100,
            "defense": 135,
            "speed": 45,
            "special": 65
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=478,
        name="Froslass",
        types=('Ice', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 80,
            "defense": 70,
            "speed": 110,
            "special": 80
        }),
        moves=('ice punch', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=479,
        name="Rotom",
        types=('Electric', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 77,
            "speed": 91,
            "special": 95
        }),
        moves=('thunder shock', 'thunderbolt', 'thunder wave', 'thunder')
    ),
    PokemonBase(
        pokedex_number=480,
        name="Uxie",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 75,
            "defense": 130,
            "speed": 95,
            "special": 75
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=481,
        name="Mesprit",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 105,
            "defense": 105,
            "speed": 80,
            "special": 105
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=482,
        name="Azelf",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 125,
            "defense": 70,
            "speed": 115,
            "special": 125
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=483,
        name="Dialga",
        types=('Steel', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 120,
            "defense": 120,
            "speed": 90,
            "special": 150
        }),
        moves=('cut', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=484,
        name="Palkia",
        types=('Water', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 120,
            "defense": 100,
            "speed": 100,
            "special": 150
        }),
        moves=('cut', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=485,
        name="Heatran",
        types=('Fire', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 90,
            "defense": 106,
            "speed": 77,
            "special": 130
        }),
        moves=('headbutt', 'body slam', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=486,
        name="Regigigas",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 160,
            "defense": 110,
            "speed": 100,
            "special": 80
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=487,
        name="Giratina-altered",
        types=('Ghost', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 150,
            "attack": 100,
            "defense": 120,
            "speed": 90,
            "special": 100
        }),
        moves=('cut', 'fly', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=488,
        name="Cresselia",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 70,
            "defense": 110,
            "speed": 85,
            "special": 75
        }),
        moves=('tackle', 'body slam', 'mist', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=489,
        name="Phione",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 80,
            "speed": 80,
            "special": 80
        }),
        moves=('supersonic', 'water gun', 'hydro pump', 'surf')
    ),
    PokemonBase(
        pokedex_number=490,
        name="Manaphy",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('supersonic', 'water gun', 'hydro pump', 'surf')
    ),
    PokemonBase(
        pokedex_number=491,
        name="Darkrai",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 90,
            "defense": 90,
            "speed": 125,
            "special": 135
        }),
        moves=('swords dance', 'cut', 'headbutt', 'disable')
    ),
    PokemonBase(
        pokedex_number=492,
        name="Shaymin-land",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('swords dance', 'headbutt', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=493,
        name="Arceus",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 120,
            "defense": 120,
            "speed": 120,
            "special": 120
        }),
        moves=('swords dance', 'cut', 'fly', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=494,
        name="Victini",
        types=('Psychic', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "speed": 100,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=495,
        name="Snivy",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 45,
            "defense": 55,
            "speed": 63,
            "special": 45
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=496,
        name="Servine",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 75,
            "speed": 83,
            "special": 60
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=497,
        name="Serperior",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 75,
            "defense": 95,
            "speed": 113,
            "special": 75
        }),
        moves=('swords dance', 'cut', 'bind', 'slam')
    ),
    PokemonBase(
        pokedex_number=498,
        name="Tepig",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 63,
            "defense": 45,
            "speed": 45,
            "special": 45
        }),
        moves=('fire punch', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=499,
        name="Pignite",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 93,
            "defense": 55,
            "speed": 55,
            "special": 70
        }),
        moves=('fire punch', 'thunder punch', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=500,
        name="Emboar",
        types=('Fire', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 123,
            "defense": 65,
            "speed": 65,
            "special": 100
        }),
        moves=('fire punch', 'thunder punch', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=501,
        name="Oshawott",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 45,
            "speed": 45,
            "special": 63
        }),
        moves=('swords dance', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=502,
        name="Dewott",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 75,
            "defense": 60,
            "speed": 60,
            "special": 83
        }),
        moves=('swords dance', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=503,
        name="Samurott",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 100,
            "defense": 85,
            "speed": 70,
            "special": 108
        }),
        moves=('swords dance', 'cut', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=504,
        name="Patrat",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 55,
            "defense": 39,
            "speed": 42,
            "special": 35
        }),
        moves=('swords dance', 'cut', 'slam', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=505,
        name="Watchog",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 69,
            "speed": 77,
            "special": 60
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=506,
        name="Lillipup",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 60,
            "defense": 45,
            "speed": 55,
            "special": 25
        }),
        moves=('sand attack', 'tackle', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=507,
        name="Herdier",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 80,
            "defense": 65,
            "speed": 60,
            "special": 35
        }),
        moves=('tackle', 'take down', 'leer', 'bite')
    ),
    PokemonBase(
        pokedex_number=508,
        name="Stoutland",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 110,
            "defense": 90,
            "speed": 80,
            "special": 45
        }),
        moves=('tackle', 'take down', 'leer', 'bite')
    ),
    PokemonBase(
        pokedex_number=509,
        name="Purrloin",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 50,
            "defense": 37,
            "speed": 66,
            "special": 50
        }),
        moves=('pay day', 'scratch', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=510,
        name="Liepard",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 64,
            "attack": 88,
            "defense": 50,
            "speed": 106,
            "special": 88
        }),
        moves=('pay day', 'scratch', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=511,
        name="Pansage",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 53,
            "defense": 48,
            "speed": 64,
            "special": 53
        }),
        moves=('scratch', 'cut', 'vine whip', 'leer')
    ),
    PokemonBase(
        pokedex_number=512,
        name="Simisage",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 98,
            "defense": 63,
            "speed": 101,
            "special": 98
        }),
        moves=('cut', 'leer', 'hyper beam', 'low kick')
    ),
    PokemonBase(
        pokedex_number=513,
        name="Pansear",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 53,
            "defense": 48,
            "speed": 64,
            "special": 53
        }),
        moves=('fire punch', 'scratch', 'cut', 'leer')
    ),
    PokemonBase(
        pokedex_number=514,
        name="Simisear",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 98,
            "defense": 63,
            "speed": 101,
            "special": 98
        }),
        moves=('fire punch', 'cut', 'leer', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=515,
        name="Panpour",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 53,
            "defense": 48,
            "speed": 64,
            "special": 53
        }),
        moves=('ice punch', 'scratch', 'cut', 'leer')
    ),
    PokemonBase(
        pokedex_number=516,
        name="Simipour",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 98,
            "defense": 63,
            "speed": 101,
            "special": 98
        }),
        moves=('ice punch', 'cut', 'leer', 'surf')
    ),
    PokemonBase(
        pokedex_number=517,
        name="Munna",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 25,
            "defense": 45,
            "speed": 24,
            "special": 67
        }),
        moves=('sonic boom', 'psybeam', 'thunder wave', 'toxic')
    ),
    PokemonBase(
        pokedex_number=518,
        name="Musharna",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 116,
            "attack": 55,
            "defense": 85,
            "speed": 29,
            "special": 107
        }),
        moves=('psybeam', 'hyper beam', 'thunder wave', 'toxic')
    ),
    PokemonBase(
        pokedex_number=519,
        name="Pidove",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 55,
            "defense": 50,
            "speed": 43,
            "special": 36
        }),
        moves=('razor wind', 'gust', 'fly', 'leer')
    ),
    PokemonBase(
        pokedex_number=520,
        name="Tranquill",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 77,
            "defense": 62,
            "speed": 65,
            "special": 50
        }),
        moves=('razor wind', 'gust', 'fly', 'leer')
    ),
    PokemonBase(
        pokedex_number=521,
        name="Unfezant",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 115,
            "defense": 80,
            "speed": 93,
            "special": 65
        }),
        moves=('razor wind', 'gust', 'fly', 'leer')
    ),
    PokemonBase(
        pokedex_number=522,
        name="Blitzle",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 60,
            "defense": 32,
            "speed": 76,
            "special": 50
        }),
        moves=('stomp', 'double kick', 'sand attack', 'body slam')
    ),
    PokemonBase(
        pokedex_number=523,
        name="Zebstrika",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 100,
            "defense": 63,
            "speed": 116,
            "special": 80
        }),
        moves=('stomp', 'double kick', 'sand attack', 'body slam')
    ),
    PokemonBase(
        pokedex_number=524,
        name="Roggenrola",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 75,
            "defense": 85,
            "speed": 15,
            "special": 25
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=525,
        name="Boldore",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 105,
            "defense": 105,
            "speed": 20,
            "special": 50
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'strength')
    ),
    PokemonBase(
        pokedex_number=526,
        name="Gigalith",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 135,
            "defense": 130,
            "speed": 25,
            "special": 60
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=527,
        name="Woobat",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 45,
            "defense": 43,
            "speed": 72,
            "special": 55
        }),
        moves=('gust', 'fly', 'supersonic', 'thunder wave')
    ),
    PokemonBase(
        pokedex_number=528,
        name="Swoobat",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 57,
            "defense": 55,
            "speed": 114,
            "special": 77
        }),
        moves=('gust', 'fly', 'hyper beam', 'thunder wave')
    ),
    PokemonBase(
        pokedex_number=529,
        name="Drilbur",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 85,
            "defense": 40,
            "speed": 68,
            "special": 30
        }),
        moves=('scratch', 'swords dance', 'cut', 'take down')
    ),
    PokemonBase(
        pokedex_number=530,
        name="Excadrill",
        types=('Ground', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 135,
            "defense": 60,
            "speed": 88,
            "special": 50
        }),
        moves=('scratch', 'swords dance', 'cut', 'horn drill')
    ),
    PokemonBase(
        pokedex_number=531,
        name="Audino",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 103,
            "attack": 60,
            "defense": 86,
            "speed": 50,
            "special": 60
        }),
        moves=('pound', 'double slap', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=532,
        name="Timburr",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 55,
            "speed": 35,
            "special": 25
        }),
        moves=('pound', 'comet punch', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=533,
        name="Gurdurr",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 105,
            "defense": 85,
            "speed": 40,
            "special": 40
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=534,
        name="Conkeldurr",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 140,
            "defense": 95,
            "speed": 45,
            "special": 55
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=535,
        name="Tympole",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 40,
            "speed": 64,
            "special": 50
        }),
        moves=('growl', 'supersonic', 'acid', 'mist')
    ),
    PokemonBase(
        pokedex_number=536,
        name="Palpitoad",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 65,
            "defense": 55,
            "speed": 69,
            "special": 65
        }),
        moves=('growl', 'supersonic', 'acid', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=537,
        name="Seismitoad",
        types=('Water', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 95,
            "defense": 75,
            "speed": 74,
            "special": 85
        }),
        moves=('mega punch', 'ice punch', 'mega kick', 'growl')
    ),
    PokemonBase(
        pokedex_number=538,
        name="Throh",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 100,
            "defense": 85,
            "speed": 45,
            "special": 30
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=539,
        name="Sawk",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 125,
            "defense": 75,
            "speed": 85,
            "special": 30
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=540,
        name="Sewaddle",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 53,
            "defense": 70,
            "speed": 42,
            "special": 40
        }),
        moves=('razor wind', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=541,
        name="Swadloon",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 63,
            "defense": 90,
            "speed": 42,
            "special": 50
        }),
        moves=('cut', 'tackle', 'take down', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=542,
        name="Leavanny",
        types=('Bug', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 103,
            "defense": 80,
            "speed": 92,
            "special": 70
        }),
        moves=('swords dance', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=543,
        name="Venipede",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 45,
            "defense": 59,
            "speed": 57,
            "special": 30
        }),
        moves=('take down', 'double edge', 'poison sting', 'twineedle')
    ),
    PokemonBase(
        pokedex_number=544,
        name="Whirlipede",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 99,
            "speed": 47,
            "special": 40
        }),
        moves=('take down', 'double edge', 'poison sting', 'pin missile')
    ),
    PokemonBase(
        pokedex_number=545,
        name="Scolipede",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 100,
            "defense": 89,
            "speed": 112,
            "special": 55
        }),
        moves=('swords dance', 'cut', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=546,
        name="Cottonee",
        types=('Grass', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 27,
            "defense": 60,
            "speed": 66,
            "special": 37
        }),
        moves=('absorb', 'mega drain', 'leech seed', 'growth')
    ),
    PokemonBase(
        pokedex_number=547,
        name="Whimsicott",
        types=('Grass', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 67,
            "defense": 85,
            "speed": 116,
            "special": 77
        }),
        moves=('gust', 'hyper beam', 'absorb', 'mega drain')
    ),
    PokemonBase(
        pokedex_number=548,
        name="Petilil",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 35,
            "defense": 50,
            "speed": 30,
            "special": 70
        }),
        moves=('cut', 'absorb', 'mega drain', 'leech seed')
    ),
    PokemonBase(
        pokedex_number=549,
        name="Lilligant",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 60,
            "defense": 75,
            "speed": 90,
            "special": 110
        }),
        moves=('swords dance', 'cut', 'hyper beam', 'absorb')
    ),
    PokemonBase(
        pokedex_number=550,
        name="Basculin-red-striped",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 92,
            "defense": 65,
            "speed": 98,
            "special": 80
        }),
        moves=('cut', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=551,
        name="Sandile",
        types=('Ground', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 72,
            "defense": 35,
            "speed": 65,
            "special": 35
        }),
        moves=('cut', 'sand attack', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=552,
        name="Krokorok",
        types=('Ground', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 82,
            "defense": 45,
            "speed": 74,
            "special": 45
        }),
        moves=('mega punch', 'cut', 'mega kick', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=553,
        name="Krookodile",
        types=('Ground', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 117,
            "defense": 80,
            "speed": 92,
            "special": 65
        }),
        moves=('mega punch', 'cut', 'mega kick', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=554,
        name="Darumaka",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 90,
            "defense": 45,
            "speed": 50,
            "special": 15
        }),
        moves=('mega punch', 'fire punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=555,
        name="Darmanitan-standard",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 140,
            "defense": 55,
            "speed": 95,
            "special": 30
        }),
        moves=('mega punch', 'fire punch', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=556,
        name="Maractus",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 86,
            "defense": 67,
            "speed": 60,
            "special": 106
        }),
        moves=('pin missile', 'peck', 'absorb', 'mega drain')
    ),
    PokemonBase(
        pokedex_number=557,
        name="Dwebble",
        types=('Bug', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 85,
            "speed": 55,
            "special": 35
        }),
        moves=('swords dance', 'cut', 'sand attack', 'counter')
    ),
    PokemonBase(
        pokedex_number=558,
        name="Crustle",
        types=('Bug', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 105,
            "defense": 125,
            "speed": 45,
            "special": 65
        }),
        moves=('swords dance', 'cut', 'sand attack', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=559,
        name="Scraggy",
        types=('Dark', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 75,
            "defense": 70,
            "speed": 48,
            "special": 35
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=560,
        name="Scrafty",
        types=('Dark', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 115,
            "speed": 58,
            "special": 45
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=561,
        name="Sigilyph",
        types=('Psychic', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 58,
            "defense": 80,
            "speed": 97,
            "special": 103
        }),
        moves=('gust', 'whirlwind', 'fly', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=562,
        name="Yamask",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 30,
            "defense": 85,
            "speed": 30,
            "special": 55
        }),
        moves=('disable', 'toxic', 'psychic', 'night shade')
    ),
    PokemonBase(
        pokedex_number=563,
        name="Cofagrigus",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 50,
            "defense": 145,
            "speed": 30,
            "special": 95
        }),
        moves=('disable', 'hyper beam', 'toxic', 'psychic')
    ),
    PokemonBase(
        pokedex_number=564,
        name="Tirtouga",
        types=('Water', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 54,
            "attack": 78,
            "defense": 103,
            "speed": 22,
            "special": 53
        }),
        moves=('slam', 'body slam', 'bite', 'water gun')
    ),
    PokemonBase(
        pokedex_number=565,
        name="Carracosta",
        types=('Water', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 108,
            "defense": 133,
            "speed": 32,
            "special": 83
        }),
        moves=('body slam', 'bite', 'water gun', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=566,
        name="Archen",
        types=('Rock', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 112,
            "defense": 45,
            "speed": 70,
            "special": 74
        }),
        moves=('cut', 'wing attack', 'thrash', 'leer')
    ),
    PokemonBase(
        pokedex_number=567,
        name="Archeops",
        types=('Rock', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 140,
            "defense": 65,
            "speed": 110,
            "special": 112
        }),
        moves=('cut', 'wing attack', 'fly', 'thrash')
    ),
    PokemonBase(
        pokedex_number=568,
        name="Trubbish",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 62,
            "speed": 65,
            "special": 40
        }),
        moves=('pound', 'double slap', 'sand attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=569,
        name="Garbodor",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 95,
            "defense": 82,
            "speed": 75,
            "special": 60
        }),
        moves=('pound', 'double slap', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=570,
        name="Zorua",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 65,
            "defense": 40,
            "speed": 65,
            "special": 80
        }),
        moves=('scratch', 'swords dance', 'cut', 'take down')
    ),
    PokemonBase(
        pokedex_number=571,
        name="Zoroark",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 105,
            "defense": 60,
            "speed": 105,
            "special": 120
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=572,
        name="Minccino",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 50,
            "defense": 40,
            "speed": 75,
            "special": 40
        }),
        moves=('pound', 'double slap', 'slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=573,
        name="Cinccino",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 95,
            "defense": 60,
            "speed": 115,
            "special": 65
        }),
        moves=('pound', 'slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=574,
        name="Gothita",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 50,
            "speed": 45,
            "special": 55
        }),
        moves=('pound', 'double slap', 'psybeam', 'thunderbolt')
    ),
    PokemonBase(
        pokedex_number=575,
        name="Gothorita",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 70,
            "speed": 55,
            "special": 75
        }),
        moves=('pound', 'double slap', 'psybeam', 'thunderbolt')
    ),
    PokemonBase(
        pokedex_number=576,
        name="Gothitelle",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 55,
            "defense": 95,
            "speed": 65,
            "special": 95
        }),
        moves=('pound', 'double slap', 'body slam', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=577,
        name="Solosis",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 40,
            "speed": 20,
            "special": 105
        }),
        moves=('psybeam', 'thunder wave', 'thunder', 'toxic')
    ),
    PokemonBase(
        pokedex_number=578,
        name="Duosion",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 40,
            "defense": 50,
            "speed": 30,
            "special": 125
        }),
        moves=('psybeam', 'thunder wave', 'thunder', 'toxic')
    ),
    PokemonBase(
        pokedex_number=579,
        name="Reuniclus",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 65,
            "defense": 75,
            "speed": 30,
            "special": 125
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=580,
        name="Ducklett",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 44,
            "defense": 50,
            "speed": 55,
            "special": 44
        }),
        moves=('gust', 'wing attack', 'fly', 'double edge')
    ),
    PokemonBase(
        pokedex_number=581,
        name="Swanna",
        types=('Water', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 87,
            "defense": 63,
            "speed": 98,
            "special": 87
        }),
        moves=('gust', 'wing attack', 'fly', 'double edge')
    ),
    PokemonBase(
        pokedex_number=582,
        name="Vanillite",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 36,
            "attack": 50,
            "defense": 50,
            "speed": 44,
            "special": 65
        }),
        moves=('mist', 'ice beam', 'blizzard', 'toxic')
    ),
    PokemonBase(
        pokedex_number=583,
        name="Vanillish",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 51,
            "attack": 65,
            "defense": 65,
            "speed": 59,
            "special": 80
        }),
        moves=('mist', 'ice beam', 'blizzard', 'toxic')
    ),
    PokemonBase(
        pokedex_number=584,
        name="Vanilluxe",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 95,
            "defense": 85,
            "speed": 79,
            "special": 110
        }),
        moves=('mist', 'ice beam', 'blizzard', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=585,
        name="Deerling",
        types=('Normal', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 50,
            "speed": 75,
            "special": 40
        }),
        moves=('double kick', 'jump kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=586,
        name="Sawsbuck",
        types=('Normal', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 100,
            "defense": 70,
            "speed": 95,
            "special": 60
        }),
        moves=('swords dance', 'cut', 'double kick', 'jump kick')
    ),
    PokemonBase(
        pokedex_number=587,
        name="Emolga",
        types=('Electric', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 75,
            "defense": 60,
            "speed": 103,
            "special": 75
        }),
        moves=('cut', 'tail whip', 'solar beam', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=588,
        name="Karrablast",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 75,
            "defense": 45,
            "speed": 60,
            "special": 40
        }),
        moves=('swords dance', 'cut', 'headbutt', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=589,
        name="Escavalier",
        types=('Bug', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 135,
            "defense": 105,
            "speed": 20,
            "special": 60
        }),
        moves=('swords dance', 'cut', 'headbutt', 'fury attack')
    ),
    PokemonBase(
        pokedex_number=590,
        name="Foongus",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 69,
            "attack": 55,
            "defense": 45,
            "speed": 15,
            "special": 55
        }),
        moves=('body slam', 'absorb', 'mega drain', 'growth')
    ),
    PokemonBase(
        pokedex_number=591,
        name="Amoonguss",
        types=('Grass', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 114,
            "attack": 85,
            "defense": 70,
            "speed": 30,
            "special": 85
        }),
        moves=('body slam', 'hyper beam', 'absorb', 'mega drain')
    ),
    PokemonBase(
        pokedex_number=592,
        name="Frillish-male",
        types=('Water', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 40,
            "defense": 50,
            "speed": 40,
            "special": 65
        }),
        moves=('bind', 'poison sting', 'mist', 'water gun')
    ),
    PokemonBase(
        pokedex_number=593,
        name="Jellicent-male",
        types=('Water', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 60,
            "defense": 70,
            "speed": 60,
            "special": 85
        }),
        moves=('bind', 'poison sting', 'water gun', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=594,
        name="Alomomola",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 165,
            "attack": 75,
            "defense": 80,
            "speed": 65,
            "special": 40
        }),
        moves=('pound', 'double slap', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=595,
        name="Joltik",
        types=('Bug', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 47,
            "defense": 50,
            "speed": 65,
            "special": 57
        }),
        moves=('cut', 'poison sting', 'pin missile', 'disable')
    ),
    PokemonBase(
        pokedex_number=596,
        name="Galvantula",
        types=('Bug', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 77,
            "defense": 60,
            "speed": 108,
            "special": 97
        }),
        moves=('cut', 'poison sting', 'pin missile', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=597,
        name="Ferroseed",
        types=('Grass', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 50,
            "defense": 91,
            "speed": 10,
            "special": 24
        }),
        moves=('tackle', 'pin missile', 'leech seed', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=598,
        name="Ferrothorn",
        types=('Grass', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 94,
            "defense": 131,
            "speed": 20,
            "special": 54
        }),
        moves=('swords dance', 'cut', 'tackle', 'pin missile')
    ),
    PokemonBase(
        pokedex_number=599,
        name="Klink",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 70,
            "speed": 30,
            "special": 45
        }),
        moves=('vice grip', 'bind', 'hyper beam', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=600,
        name="Klang",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 80,
            "defense": 95,
            "speed": 50,
            "special": 70
        }),
        moves=('vice grip', 'bind', 'hyper beam', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=601,
        name="Klinklang",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 100,
            "defense": 115,
            "speed": 90,
            "special": 70
        }),
        moves=('vice grip', 'bind', 'hyper beam', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=602,
        name="Tynamo",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 55,
            "defense": 40,
            "speed": 60,
            "special": 45
        }),
        moves=('tackle', 'thunder wave', 'spark', 'charge')
    ),
    PokemonBase(
        pokedex_number=603,
        name="Eelektrik",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 85,
            "defense": 70,
            "speed": 40,
            "special": 75
        }),
        moves=('bind', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=604,
        name="Eelektross",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 115,
            "defense": 80,
            "speed": 50,
            "special": 105
        }),
        moves=('fire punch', 'thunder punch', 'cut', 'bind')
    ),
    PokemonBase(
        pokedex_number=605,
        name="Elgyem",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 55,
            "speed": 30,
            "special": 85
        }),
        moves=('headbutt', 'growl', 'disable', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=606,
        name="Beheeyem",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 75,
            "defense": 75,
            "speed": 40,
            "special": 125
        }),
        moves=('headbutt', 'growl', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=607,
        name="Litwick",
        types=('Ghost', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 30,
            "defense": 55,
            "speed": 20,
            "special": 65
        }),
        moves=('acid', 'ember', 'flamethrower', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=608,
        name="Lampent",
        types=('Ghost', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 40,
            "defense": 60,
            "speed": 55,
            "special": 95
        }),
        moves=('ember', 'flamethrower', 'solar beam', 'fire spin')
    ),
    PokemonBase(
        pokedex_number=609,
        name="Chandelure",
        types=('Ghost', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 55,
            "defense": 90,
            "speed": 80,
            "special": 145
        }),
        moves=('ember', 'flamethrower', 'hyper beam', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=610,
        name="Axew",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 46,
            "attack": 87,
            "defense": 60,
            "speed": 57,
            "special": 30
        }),
        moves=('scratch', 'guillotine', 'razor wind', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=611,
        name="Fraxure",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 66,
            "attack": 117,
            "defense": 70,
            "speed": 67,
            "special": 40
        }),
        moves=('scratch', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=612,
        name="Haxorus",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 147,
            "defense": 90,
            "speed": 97,
            "special": 60
        }),
        moves=('scratch', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=613,
        name="Cubchoo",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 70,
            "defense": 40,
            "speed": 40,
            "special": 60
        }),
        moves=('mega punch', 'ice punch', 'cut', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=614,
        name="Beartic",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 130,
            "defense": 80,
            "speed": 50,
            "special": 70
        }),
        moves=('mega punch', 'ice punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=615,
        name="Cryogonal",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 50,
            "defense": 50,
            "speed": 105,
            "special": 95
        }),
        moves=('bind', 'body slam', 'take down', 'mist')
    ),
    PokemonBase(
        pokedex_number=616,
        name="Shelmet",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 40,
            "defense": 85,
            "speed": 25,
            "special": 40
        }),
        moves=('body slam', 'double edge', 'acid', 'absorb')
    ),
    PokemonBase(
        pokedex_number=617,
        name="Accelgor",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 70,
            "defense": 40,
            "speed": 145,
            "special": 100
        }),
        moves=('body slam', 'acid', 'hyper beam', 'absorb')
    ),
    PokemonBase(
        pokedex_number=618,
        name="Stunfisk",
        types=('Ground', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 109,
            "attack": 66,
            "defense": 84,
            "speed": 32,
            "special": 81
        }),
        moves=('tackle', 'water gun', 'surf', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=619,
        name="Mienfoo",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 85,
            "defense": 50,
            "speed": 65,
            "special": 55
        }),
        moves=('pound', 'double slap', 'mega punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=620,
        name="Mienshao",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 125,
            "defense": 60,
            "speed": 105,
            "special": 95
        }),
        moves=('pound', 'double slap', 'mega punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=621,
        name="Druddigon",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 77,
            "attack": 120,
            "defense": 90,
            "speed": 48,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=622,
        name="Golett",
        types=('Ground', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 74,
            "defense": 50,
            "speed": 35,
            "special": 35
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=623,
        name="Golurk",
        types=('Ground', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 89,
            "attack": 124,
            "defense": 80,
            "speed": 55,
            "special": 55
        }),
        moves=('pound', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=624,
        name="Pawniard",
        types=('Dark', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 85,
            "defense": 70,
            "speed": 60,
            "special": 40
        }),
        moves=('scratch', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=625,
        name="Bisharp",
        types=('Dark', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 125,
            "defense": 100,
            "speed": 70,
            "special": 60
        }),
        moves=('scratch', 'guillotine', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=626,
        name="Bouffalant",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 110,
            "defense": 95,
            "speed": 55,
            "special": 40
        }),
        moves=('swords dance', 'cut', 'stomp', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=627,
        name="Rufflet",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 83,
            "defense": 50,
            "speed": 60,
            "special": 37
        }),
        moves=('cut', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=628,
        name="Braviary",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 123,
            "defense": 75,
            "speed": 80,
            "special": 57
        }),
        moves=('cut', 'wing attack', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=629,
        name="Vullaby",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 55,
            "defense": 75,
            "speed": 60,
            "special": 45
        }),
        moves=('cut', 'gust', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=630,
        name="Mandibuzz",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 65,
            "defense": 105,
            "speed": 80,
            "special": 55
        }),
        moves=('cut', 'gust', 'whirlwind', 'fly')
    ),
    PokemonBase(
        pokedex_number=631,
        name="Heatmor",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 97,
            "defense": 66,
            "speed": 65,
            "special": 105
        }),
        moves=('fire punch', 'thunder punch', 'cut', 'bind')
    ),
    PokemonBase(
        pokedex_number=632,
        name="Durant",
        types=('Bug', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 109,
            "defense": 112,
            "speed": 109,
            "special": 48
        }),
        moves=('vice grip', 'guillotine', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=633,
        name="Deino",
        types=('Dark', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 52,
            "attack": 65,
            "defense": 50,
            "speed": 38,
            "special": 45
        }),
        moves=('slam', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=634,
        name="Zweilous",
        types=('Dark', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 85,
            "defense": 70,
            "speed": 58,
            "special": 65
        }),
        moves=('slam', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=635,
        name="Hydreigon",
        types=('Dark', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 92,
            "attack": 105,
            "defense": 90,
            "speed": 98,
            "special": 125
        }),
        moves=('fly', 'slam', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=636,
        name="Larvesta",
        types=('Bug', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 85,
            "defense": 55,
            "speed": 60,
            "special": 50
        }),
        moves=('body slam', 'take down', 'thrash', 'double edge')
    ),
    PokemonBase(
        pokedex_number=637,
        name="Volcarona",
        types=('Bug', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 60,
            "defense": 65,
            "speed": 100,
            "special": 135
        }),
        moves=('gust', 'whirlwind', 'fly', 'body slam')
    ),
    PokemonBase(
        pokedex_number=638,
        name="Cobalion",
        types=('Steel', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 90,
            "defense": 129,
            "speed": 108,
            "special": 90
        }),
        moves=('swords dance', 'cut', 'double kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=639,
        name="Terrakion",
        types=('Rock', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 129,
            "defense": 90,
            "speed": 108,
            "special": 72
        }),
        moves=('swords dance', 'cut', 'double kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=640,
        name="Virizion",
        types=('Grass', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 90,
            "defense": 72,
            "speed": 108,
            "special": 90
        }),
        moves=('swords dance', 'cut', 'double kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=641,
        name="Tornadus-incarnate",
        types=('Flying',),
        base_stats=MappingProxyType({
            "hp": 79,
            "attack": 115,
            "defense": 70,
            "speed": 111,
            "special": 125
        }),
        moves=('gust', 'fly', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=642,
        name="Thundurus-incarnate",
        types=('Electric', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 79,
            "attack": 115,
            "defense": 70,
            "speed": 111,
            "special": 125
        }),
        moves=('thunder punch', 'fly', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=643,
        name="Reshiram",
        types=('Dragon', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 120,
            "defense": 100,
            "speed": 90,
            "special": 150
        }),
        moves=('cut', 'fly', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=644,
        name="Zekrom",
        types=('Dragon', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 150,
            "defense": 120,
            "speed": 90,
            "special": 120
        }),
        moves=('thunder punch', 'cut', 'fly', 'body slam')
    ),
    PokemonBase(
        pokedex_number=645,
        name="Landorus-incarnate",
        types=('Ground', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 89,
            "attack": 125,
            "defense": 90,
            "speed": 101,
            "special": 115
        }),
        moves=('swords dance', 'fly', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=646,
        name="Kyurem",
        types=('Dragon', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 125,
            "attack": 130,
            "defense": 90,
            "speed": 95,
            "special": 130
        }),
        moves=('cut', 'fly', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=647,
        name="Keldeo-ordinary",
        types=('Water', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 91,
            "attack": 72,
            "defense": 90,
            "speed": 108,
            "special": 129
        }),
        moves=('swords dance', 'cut', 'double kick', 'take down')
    ),
    PokemonBase(
        pokedex_number=648,
        name="Meloetta-aria",
        types=('Normal', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 77,
            "defense": 77,
            "speed": 90,
            "special": 128
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=649,
        name="Genesect",
        types=('Bug', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 120,
            "defense": 95,
            "speed": 99,
            "special": 120
        }),
        moves=('fly', 'flamethrower', 'ice beam', 'blizzard')
    ),
    PokemonBase(
        pokedex_number=650,
        name="Chespin",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 56,
            "attack": 61,
            "defense": 65,
            "speed": 38,
            "special": 48
        }),
        moves=('thunder punch', 'swords dance', 'cut', 'vine whip')
    ),
    PokemonBase(
        pokedex_number=651,
        name="Quilladin",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 78,
            "defense": 95,
            "speed": 57,
            "special": 56
        }),
        moves=('thunder punch', 'swords dance', 'cut', 'vine whip')
    ),
    PokemonBase(
        pokedex_number=652,
        name="Chesnaught",
        types=('Grass', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 107,
            "defense": 122,
            "speed": 64,
            "special": 74
        }),
        moves=('thunder punch', 'swords dance', 'cut', 'vine whip')
    ),
    PokemonBase(
        pokedex_number=653,
        name="Fennekin",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 40,
            "speed": 60,
            "special": 62
        }),
        moves=('scratch', 'cut', 'take down', 'tail whip')
    ),
    PokemonBase(
        pokedex_number=654,
        name="Braixen",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 59,
            "defense": 58,
            "speed": 73,
            "special": 90
        }),
        moves=('fire punch', 'thunder punch', 'scratch', 'cut')
    ),
    PokemonBase(
        pokedex_number=655,
        name="Delphox",
        types=('Fire', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 69,
            "defense": 72,
            "speed": 104,
            "special": 114
        }),
        moves=('fire punch', 'thunder punch', 'scratch', 'cut')
    ),
    PokemonBase(
        pokedex_number=656,
        name="Froakie",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 56,
            "defense": 40,
            "speed": 71,
            "special": 62
        }),
        moves=('pound', 'cut', 'take down', 'growl')
    ),
    PokemonBase(
        pokedex_number=657,
        name="Frogadier",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 54,
            "attack": 63,
            "defense": 52,
            "speed": 97,
            "special": 83
        }),
        moves=('pound', 'ice punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=658,
        name="Greninja",
        types=('Water', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 95,
            "defense": 67,
            "speed": 122,
            "special": 103
        }),
        moves=('pound', 'ice punch', 'swords dance', 'cut')
    ),
    PokemonBase(
        pokedex_number=659,
        name="Bunnelby",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 36,
            "defense": 38,
            "speed": 57,
            "special": 32
        }),
        moves=('double slap', 'swords dance', 'cut', 'double kick')
    ),
    PokemonBase(
        pokedex_number=660,
        name="Diggersby",
        types=('Normal', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 56,
            "defense": 77,
            "speed": 78,
            "special": 50
        }),
        moves=('double slap', 'mega punch', 'fire punch', 'ice punch')
    ),
    PokemonBase(
        pokedex_number=661,
        name="Fletchling",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 50,
            "defense": 43,
            "speed": 62,
            "special": 40
        }),
        moves=('razor wind', 'swords dance', 'fly', 'tackle')
    ),
    PokemonBase(
        pokedex_number=662,
        name="Fletchinder",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 73,
            "defense": 55,
            "speed": 84,
            "special": 56
        }),
        moves=('razor wind', 'swords dance', 'fly', 'tackle')
    ),
    PokemonBase(
        pokedex_number=663,
        name="Talonflame",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 81,
            "defense": 71,
            "speed": 126,
            "special": 74
        }),
        moves=('razor wind', 'swords dance', 'fly', 'tackle')
    ),
    PokemonBase(
        pokedex_number=664,
        name="Scatterbug",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 35,
            "defense": 40,
            "speed": 35,
            "special": 27
        }),
        moves=('tackle', 'poison powder', 'stun spore', 'string shot')
    ),
    PokemonBase(
        pokedex_number=665,
        name="Spewpa",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 22,
            "defense": 60,
            "speed": 29,
            "special": 27
        }),
        moves=('harden', 'protect', 'iron defense', 'bug bite')
    ),
    PokemonBase(
        pokedex_number=666,
        name="Vivillon",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 52,
            "defense": 50,
            "speed": 89,
            "special": 90
        }),
        moves=('gust', 'supersonic', 'psybeam', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=667,
        name="Litleo",
        types=('Fire', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 50,
            "defense": 58,
            "speed": 72,
            "special": 73
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=668,
        name="Pyroar-male",
        types=('Fire', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 86,
            "attack": 68,
            "defense": 72,
            "speed": 106,
            "special": 109
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=669,
        name="Flabebe",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 38,
            "defense": 39,
            "speed": 42,
            "special": 61
        }),
        moves=('vine whip', 'tackle', 'razor leaf', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=670,
        name="Floette",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 54,
            "attack": 45,
            "defense": 47,
            "speed": 52,
            "special": 75
        }),
        moves=('vine whip', 'tackle', 'razor leaf', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=671,
        name="Florges",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 65,
            "defense": 68,
            "speed": 75,
            "special": 112
        }),
        moves=('hyper beam', 'solar beam', 'petal dance', 'toxic')
    ),
    PokemonBase(
        pokedex_number=672,
        name="Skiddo",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 66,
            "attack": 65,
            "defense": 48,
            "speed": 52,
            "special": 62
        }),
        moves=('vine whip', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=673,
        name="Gogoat",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 123,
            "attack": 100,
            "defense": 62,
            "speed": 68,
            "special": 97
        }),
        moves=('vine whip', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=674,
        name="Pancham",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 82,
            "defense": 62,
            "speed": 43,
            "special": 46
        }),
        moves=('karate chop', 'comet punch', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=675,
        name="Pangoro",
        types=('Fighting', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 124,
            "defense": 78,
            "speed": 58,
            "special": 69
        }),
        moves=('karate chop', 'comet punch', 'mega punch', 'fire punch')
    ),
    PokemonBase(
        pokedex_number=676,
        name="Furfrou",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 60,
            "speed": 102,
            "special": 65
        }),
        moves=('sand attack', 'headbutt', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=677,
        name="Espurr",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 48,
            "defense": 54,
            "speed": 68,
            "special": 63
        }),
        moves=('pay day', 'scratch', 'cut', 'leer')
    ),
    PokemonBase(
        pokedex_number=678,
        name="Meowstic-male",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 48,
            "defense": 76,
            "speed": 104,
            "special": 83
        }),
        moves=('pay day', 'scratch', 'cut', 'leer')
    ),
    PokemonBase(
        pokedex_number=679,
        name="Honedge",
        types=('Steel', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 80,
            "defense": 100,
            "speed": 28,
            "special": 35
        }),
        moves=('swords dance', 'cut', 'tackle', 'toxic')
    ),
    PokemonBase(
        pokedex_number=680,
        name="Doublade",
        types=('Steel', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 110,
            "defense": 150,
            "speed": 35,
            "special": 45
        }),
        moves=('swords dance', 'cut', 'tackle', 'toxic')
    ),
    PokemonBase(
        pokedex_number=681,
        name="Aegislash-shield",
        types=('Steel', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 140,
            "speed": 60,
            "special": 50
        }),
        moves=('swords dance', 'cut', 'tackle', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=682,
        name="Spritzee",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 52,
            "defense": 60,
            "speed": 23,
            "special": 63
        }),
        moves=('disable', 'thunderbolt', 'toxic', 'psychic')
    ),
    PokemonBase(
        pokedex_number=683,
        name="Aromatisse",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 101,
            "attack": 72,
            "defense": 72,
            "speed": 29,
            "special": 99
        }),
        moves=('hyper beam', 'thunderbolt', 'thunder', 'toxic')
    ),
    PokemonBase(
        pokedex_number=684,
        name="Swirlix",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 48,
            "defense": 66,
            "speed": 49,
            "special": 59
        }),
        moves=('tackle', 'flamethrower', 'surf', 'string shot')
    ),
    PokemonBase(
        pokedex_number=685,
        name="Slurpuff",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 82,
            "attack": 80,
            "defense": 86,
            "speed": 72,
            "special": 85
        }),
        moves=('tackle', 'flamethrower', 'surf', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=686,
        name="Inkay",
        types=('Dark', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 53,
            "attack": 54,
            "defense": 53,
            "speed": 45,
            "special": 37
        }),
        moves=('cut', 'bind', 'tackle', 'wrap')
    ),
    PokemonBase(
        pokedex_number=687,
        name="Malamar",
        types=('Dark', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 86,
            "attack": 92,
            "defense": 88,
            "speed": 73,
            "special": 68
        }),
        moves=('cut', 'bind', 'tackle', 'wrap')
    ),
    PokemonBase(
        pokedex_number=688,
        name="Binacle",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 42,
            "attack": 52,
            "defense": 67,
            "speed": 50,
            "special": 39
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=689,
        name="Barbaracle",
        types=('Rock', 'Water'),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 105,
            "defense": 115,
            "speed": 68,
            "special": 54
        }),
        moves=('scratch', 'swords dance', 'cut', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=690,
        name="Skrelp",
        types=('Poison', 'Water'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 60,
            "defense": 60,
            "speed": 30,
            "special": 60
        }),
        moves=('tackle', 'take down', 'tail whip', 'acid')
    ),
    PokemonBase(
        pokedex_number=691,
        name="Dragalge",
        types=('Poison', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 75,
            "defense": 90,
            "speed": 44,
            "special": 97
        }),
        moves=('tackle', 'take down', 'tail whip', 'acid')
    ),
    PokemonBase(
        pokedex_number=692,
        name="Clauncher",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 53,
            "defense": 62,
            "speed": 44,
            "special": 58
        }),
        moves=('vice grip', 'swords dance', 'cut', 'take down')
    ),
    PokemonBase(
        pokedex_number=693,
        name="Clawitzer",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 73,
            "defense": 88,
            "speed": 59,
            "special": 120
        }),
        moves=('vice grip', 'swords dance', 'cut', 'body slam')
    ),
    PokemonBase(
        pokedex_number=694,
        name="Helioptile",
        types=('Electric', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 44,
            "attack": 38,
            "defense": 33,
            "speed": 70,
            "special": 61
        }),
        moves=('pound', 'razor wind', 'cut', 'tail whip')
    ),
    PokemonBase(
        pokedex_number=695,
        name="Heliolisk",
        types=('Electric', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 55,
            "defense": 52,
            "speed": 109,
            "special": 109
        }),
        moves=('pound', 'mega punch', 'fire punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=696,
        name="Tyrunt",
        types=('Rock', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 89,
            "defense": 77,
            "speed": 48,
            "special": 45
        }),
        moves=('stomp', 'horn drill', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=697,
        name="Tyrantrum",
        types=('Rock', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 82,
            "attack": 121,
            "defense": 119,
            "speed": 71,
            "special": 69
        }),
        moves=('stomp', 'horn drill', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=698,
        name="Amaura",
        types=('Rock', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 77,
            "attack": 59,
            "defense": 50,
            "speed": 46,
            "special": 67
        }),
        moves=('body slam', 'take down', 'growl', 'roar')
    ),
    PokemonBase(
        pokedex_number=699,
        name="Aurorus",
        types=('Rock', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 123,
            "attack": 77,
            "defense": 72,
            "speed": 58,
            "special": 99
        }),
        moves=('body slam', 'take down', 'growl', 'roar')
    ),
    PokemonBase(
        pokedex_number=700,
        name="Sylveon",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 65,
            "defense": 65,
            "speed": 60,
            "special": 110
        }),
        moves=('pay day', 'cut', 'sand attack', 'tackle')
    ),
    PokemonBase(
        pokedex_number=701,
        name="Hawlucha",
        types=('Fighting', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 92,
            "defense": 75,
            "speed": 118,
            "special": 74
        }),
        moves=('karate chop', 'mega punch', 'fire punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=702,
        name="Dedenne",
        types=('Electric', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 58,
            "defense": 57,
            "speed": 101,
            "special": 81
        }),
        moves=('thunder punch', 'cut', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=703,
        name="Carbink",
        types=('Rock', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 150,
            "speed": 50,
            "special": 50
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=704,
        name="Goomy",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 50,
            "defense": 35,
            "speed": 40,
            "special": 55
        }),
        moves=('tackle', 'body slam', 'take down', 'water gun')
    ),
    PokemonBase(
        pokedex_number=705,
        name="Sliggoo",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 75,
            "defense": 53,
            "speed": 60,
            "special": 83
        }),
        moves=('tackle', 'body slam', 'take down', 'water gun')
    ),
    PokemonBase(
        pokedex_number=706,
        name="Goodra",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 100,
            "defense": 70,
            "speed": 80,
            "special": 110
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=707,
        name="Klefki",
        types=('Steel', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 80,
            "defense": 91,
            "speed": 75,
            "special": 80
        }),
        moves=('cut', 'tackle', 'hyper beam', 'thunder wave')
    ),
    PokemonBase(
        pokedex_number=708,
        name="Phantump",
        types=('Ghost', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 43,
            "attack": 70,
            "defense": 48,
            "speed": 38,
            "special": 50
        }),
        moves=('cut', 'tackle', 'disable', 'strength')
    ),
    PokemonBase(
        pokedex_number=709,
        name="Trevenant",
        types=('Ghost', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 110,
            "defense": 76,
            "speed": 56,
            "special": 65
        }),
        moves=('cut', 'tackle', 'take down', 'disable')
    ),
    PokemonBase(
        pokedex_number=710,
        name="Pumpkaboo-average",
        types=('Ghost', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 49,
            "attack": 66,
            "defense": 70,
            "speed": 51,
            "special": 44
        }),
        moves=('disable', 'flamethrower', 'leech seed', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=711,
        name="Gourgeist-average",
        types=('Ghost', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 122,
            "speed": 84,
            "special": 58
        }),
        moves=('flamethrower', 'hyper beam', 'leech seed', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=712,
        name="Bergmite",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 69,
            "defense": 85,
            "speed": 28,
            "special": 32
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=713,
        name="Avalugg",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 117,
            "defense": 184,
            "speed": 28,
            "special": 44
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=714,
        name="Noibat",
        types=('Flying', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 30,
            "defense": 35,
            "speed": 55,
            "special": 45
        }),
        moves=('razor wind', 'cut', 'gust', 'wing attack')
    ),
    PokemonBase(
        pokedex_number=715,
        name="Noivern",
        types=('Flying', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 70,
            "defense": 80,
            "speed": 123,
            "special": 97
        }),
        moves=('razor wind', 'cut', 'gust', 'wing attack')
    ),
    PokemonBase(
        pokedex_number=716,
        name="Xerneas",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 126,
            "attack": 131,
            "defense": 95,
            "speed": 99,
            "special": 131
        }),
        moves=('cut', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=717,
        name="Yveltal",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 126,
            "attack": 131,
            "defense": 95,
            "speed": 99,
            "special": 131
        }),
        moves=('razor wind', 'cut', 'gust', 'fly')
    ),
    PokemonBase(
        pokedex_number=718,
        name="Zygarde-50",
        types=('Dragon', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 108,
            "attack": 100,
            "defense": 121,
            "speed": 95,
            "special": 81
        }),
        moves=('bind', 'body slam', 'bite', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=719,
        name="Diancie",
        types=('Rock', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 100,
            "defense": 150,
            "speed": 50,
            "special": 100
        }),
        moves=('tackle', 'body slam', 'take down', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=720,
        name="Hoopa",
        types=('Psychic', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 110,
            "defense": 60,
            "speed": 70,
            "special": 150
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'take down')
    ),
    PokemonBase(
        pokedex_number=721,
        name="Volcanion",
        types=('Fire', 'Water'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 110,
            "defense": 120,
            "speed": 70,
            "special": 130
        }),
        moves=('cut', 'stomp', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=722,
        name="Rowlet",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 55,
            "defense": 55,
            "speed": 42,
            "special": 50
        }),
        moves=('swords dance', 'gust', 'fury attack', 'tackle')
    ),
    PokemonBase(
        pokedex_number=723,
        name="Dartrix",
        types=('Grass', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 75,
            "defense": 75,
            "speed": 52,
            "special": 70
        }),
        moves=('swords dance', 'gust', 'fury attack', 'tackle')
    ),
    PokemonBase(
        pokedex_number=724,
        name="Decidueye",
        types=('Grass', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 107,
            "defense": 75,
            "speed": 70,
            "special": 100
        }),
        moves=('swords dance', 'fury attack', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=725,
        name="Litten",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 65,
            "defense": 40,
            "speed": 70,
            "special": 60
        }),
        moves=('pay day', 'scratch', 'swords dance', 'double kick')
    ),
    PokemonBase(
        pokedex_number=726,
        name="Torracat",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 85,
            "defense": 50,
            "speed": 90,
            "special": 80
        }),
        moves=('pay day', 'scratch', 'swords dance', 'double kick')
    ),
    PokemonBase(
        pokedex_number=727,
        name="Incineroar",
        types=('Fire', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 115,
            "defense": 90,
            "speed": 60,
            "special": 80
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=728,
        name="Popplio",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 54,
            "defense": 54,
            "speed": 40,
            "special": 66
        }),
        moves=('pound', 'double slap', 'growl', 'sing')
    ),
    PokemonBase(
        pokedex_number=729,
        name="Brionne",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 69,
            "defense": 69,
            "speed": 50,
            "special": 91
        }),
        moves=('pound', 'double slap', 'body slam', 'growl')
    ),
    PokemonBase(
        pokedex_number=730,
        name="Primarina",
        types=('Water', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 74,
            "defense": 74,
            "speed": 60,
            "special": 126
        }),
        moves=('pound', 'double slap', 'body slam', 'growl')
    ),
    PokemonBase(
        pokedex_number=731,
        name="Pikipek",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 75,
            "defense": 30,
            "speed": 65,
            "special": 30
        }),
        moves=('swords dance', 'fly', 'fury attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=732,
        name="Trumbeak",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 85,
            "defense": 50,
            "speed": 75,
            "special": 40
        }),
        moves=('swords dance', 'fly', 'fury attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=733,
        name="Toucannon",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 75,
            "speed": 60,
            "special": 75
        }),
        moves=('swords dance', 'fly', 'fury attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=734,
        name="Yungoos",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 70,
            "defense": 30,
            "speed": 45,
            "special": 30
        }),
        moves=('sand attack', 'tackle', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=735,
        name="Gumshoos",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 110,
            "defense": 60,
            "speed": 45,
            "special": 55
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=736,
        name="Grubbin",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 47,
            "attack": 62,
            "defense": 45,
            "speed": 46,
            "special": 55
        }),
        moves=('vice grip', 'take down', 'bite', 'string shot')
    ),
    PokemonBase(
        pokedex_number=737,
        name="Charjabug",
        types=('Bug', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 82,
            "defense": 95,
            "speed": 36,
            "special": 55
        }),
        moves=('vice grip', 'take down', 'bite', 'string shot')
    ),
    PokemonBase(
        pokedex_number=738,
        name="Vikavolt",
        types=('Bug', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 77,
            "attack": 70,
            "defense": 90,
            "speed": 43,
            "special": 145
        }),
        moves=('vice grip', 'guillotine', 'fly', 'take down')
    ),
    PokemonBase(
        pokedex_number=739,
        name="Crabrawler",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 47,
            "attack": 82,
            "defense": 57,
            "speed": 63,
            "special": 42
        }),
        moves=('ice punch', 'thunder punch', 'slam', 'body slam')
    ),
    PokemonBase(
        pokedex_number=740,
        name="Crabominable",
        types=('Fighting', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 97,
            "attack": 132,
            "defense": 77,
            "speed": 43,
            "special": 62
        }),
        moves=('ice punch', 'thunder punch', 'slam', 'body slam')
    ),
    PokemonBase(
        pokedex_number=741,
        name="Oricorio-baile",
        types=('Fire', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 70,
            "defense": 70,
            "speed": 93,
            "special": 98
        }),
        moves=('pound', 'double slap', 'swords dance', 'fly')
    ),
    PokemonBase(
        pokedex_number=742,
        name="Cutiefly",
        types=('Bug', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 40,
            "speed": 84,
            "special": 55
        }),
        moves=('absorb', 'stun spore', 'toxic', 'psychic')
    ),
    PokemonBase(
        pokedex_number=743,
        name="Ribombee",
        types=('Bug', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 55,
            "defense": 60,
            "speed": 124,
            "special": 95
        }),
        moves=('take down', 'hyper beam', 'absorb', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=744,
        name="Rockruff",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 65,
            "defense": 40,
            "speed": 60,
            "special": 30
        }),
        moves=('swords dance', 'sand attack', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=745,
        name="Lycanroc-midday",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 115,
            "defense": 65,
            "speed": 112,
            "special": 55
        }),
        moves=('swords dance', 'sand attack', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=746,
        name="Wishiwashi-solo",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 20,
            "defense": 20,
            "speed": 40,
            "special": 25
        }),
        moves=('take down', 'double edge', 'growl', 'mist')
    ),
    PokemonBase(
        pokedex_number=747,
        name="Mareanie",
        types=('Poison', 'Water'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 53,
            "defense": 62,
            "speed": 45,
            "special": 43
        }),
        moves=('poison sting', 'pin missile', 'bite', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=748,
        name="Toxapex",
        types=('Poison', 'Water'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 63,
            "defense": 152,
            "speed": 35,
            "special": 53
        }),
        moves=('body slam', 'poison sting', 'pin missile', 'bite')
    ),
    PokemonBase(
        pokedex_number=749,
        name="Mudbray",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 100,
            "defense": 70,
            "speed": 45,
            "special": 45
        }),
        moves=('stomp', 'double kick', 'mega kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=750,
        name="Mudsdale",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 125,
            "defense": 100,
            "speed": 35,
            "special": 55
        }),
        moves=('stomp', 'double kick', 'mega kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=751,
        name="Dewpider",
        types=('Water', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 40,
            "defense": 52,
            "speed": 27,
            "special": 40
        }),
        moves=('headbutt', 'bite', 'water gun', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=752,
        name="Araquanid",
        types=('Water', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 70,
            "defense": 92,
            "speed": 42,
            "special": 50
        }),
        moves=('headbutt', 'body slam', 'bite', 'water gun')
    ),
    PokemonBase(
        pokedex_number=753,
        name="Fomantis",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 55,
            "defense": 35,
            "speed": 35,
            "special": 50
        }),
        moves=('swords dance', 'take down', 'growth', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=754,
        name="Lurantis",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 105,
            "defense": 90,
            "speed": 45,
            "special": 80
        }),
        moves=('swords dance', 'take down', 'hyper beam', 'growth')
    ),
    PokemonBase(
        pokedex_number=755,
        name="Morelull",
        types=('Grass', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 35,
            "defense": 55,
            "speed": 15,
            "special": 65
        }),
        moves=('absorb', 'mega drain', 'leech seed', 'growth')
    ),
    PokemonBase(
        pokedex_number=756,
        name="Shiinotic",
        types=('Grass', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 80,
            "speed": 30,
            "special": 90
        }),
        moves=('hyper beam', 'absorb', 'mega drain', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=757,
        name="Salandit",
        types=('Poison', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 44,
            "defense": 40,
            "speed": 77,
            "special": 71
        }),
        moves=('double slap', 'scratch', 'sand attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=758,
        name="Salazzle",
        types=('Poison', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 64,
            "defense": 60,
            "speed": 117,
            "special": 111
        }),
        moves=('pound', 'double slap', 'scratch', 'body slam')
    ),
    PokemonBase(
        pokedex_number=759,
        name="Stufful",
        types=('Normal', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 75,
            "defense": 50,
            "speed": 50,
            "special": 45
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=760,
        name="Bewear",
        types=('Normal', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 125,
            "defense": 80,
            "speed": 60,
            "special": 55
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=761,
        name="Bounsweet",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 42,
            "attack": 30,
            "defense": 38,
            "speed": 32,
            "special": 30
        }),
        moves=('take down', 'razor leaf', 'solar beam', 'toxic')
    ),
    PokemonBase(
        pokedex_number=762,
        name="Steenee",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 52,
            "attack": 40,
            "defense": 48,
            "speed": 62,
            "special": 40
        }),
        moves=('double slap', 'stomp', 'take down', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=763,
        name="Tsareena",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 120,
            "defense": 98,
            "speed": 72,
            "special": 50
        }),
        moves=('double slap', 'stomp', 'mega kick', 'take down')
    ),
    PokemonBase(
        pokedex_number=764,
        name="Comfey",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 51,
            "attack": 52,
            "defense": 90,
            "speed": 100,
            "special": 82
        }),
        moves=('bind', 'vine whip', 'wrap', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=765,
        name="Oranguru",
        types=('Normal', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 60,
            "defense": 80,
            "speed": 60,
            "special": 90
        }),
        moves=('mega punch', 'mega kick', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=766,
        name="Passimian",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 120,
            "defense": 90,
            "speed": 80,
            "special": 40
        }),
        moves=('mega punch', 'mega kick', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=767,
        name="Wimpod",
        types=('Bug', 'Water'),
        base_stats=MappingProxyType({
            "hp": 25,
            "attack": 35,
            "defense": 40,
            "speed": 80,
            "special": 20
        }),
        moves=('sand attack', 'surf', 'toxic', 'screech')
    ),
    PokemonBase(
        pokedex_number=768,
        name="Golisopod",
        types=('Bug', 'Water'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 125,
            "defense": 140,
            "speed": 40,
            "special": 60
        }),
        moves=('swords dance', 'sand attack', 'pin missile', 'surf')
    ),
    PokemonBase(
        pokedex_number=769,
        name="Sandygast",
        types=('Ghost', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 80,
            "speed": 15,
            "special": 70
        }),
        moves=('sand attack', 'absorb', 'mega drain', 'earthquake')
    ),
    PokemonBase(
        pokedex_number=770,
        name="Palossand",
        types=('Ghost', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 75,
            "defense": 110,
            "speed": 35,
            "special": 100
        }),
        moves=('sand attack', 'body slam', 'hyper beam', 'absorb')
    ),
    PokemonBase(
        pokedex_number=771,
        name="Pyukumuku",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 60,
            "defense": 130,
            "speed": 5,
            "special": 30
        }),
        moves=('counter', 'toxic', 'screech', 'double team')
    ),
    PokemonBase(
        pokedex_number=772,
        name="Type-null",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 95,
            "defense": 95,
            "speed": 59,
            "special": 95
        }),
        moves=('razor wind', 'swords dance', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=773,
        name="Silvally",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 95,
            "defense": 95,
            "speed": 95,
            "special": 95
        }),
        moves=('razor wind', 'swords dance', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=774,
        name="Minior-red-meteor",
        types=('Rock', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 100,
            "speed": 60,
            "special": 60
        }),
        moves=('tackle', 'take down', 'double edge', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=775,
        name="Komala",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 115,
            "defense": 65,
            "speed": 65,
            "special": 75
        }),
        moves=('swords dance', 'slam', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=776,
        name="Turtonator",
        types=('Fire', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 78,
            "defense": 135,
            "speed": 36,
            "special": 91
        }),
        moves=('mega punch', 'mega kick', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=777,
        name="Togedemaru",
        types=('Electric', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 98,
            "defense": 63,
            "speed": 96,
            "special": 40
        }),
        moves=('tackle', 'twineedle', 'pin missile', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=778,
        name="Mimikyu-disguised",
        types=('Ghost', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 90,
            "defense": 80,
            "speed": 96,
            "special": 50
        }),
        moves=('scratch', 'swords dance', 'take down', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=779,
        name="Bruxish",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 105,
            "defense": 70,
            "speed": 92,
            "special": 70
        }),
        moves=('swords dance', 'take down', 'bite', 'disable')
    ),
    PokemonBase(
        pokedex_number=780,
        name="Drampa",
        types=('Normal', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 60,
            "defense": 85,
            "speed": 36,
            "special": 135
        }),
        moves=('razor wind', 'fly', 'roar', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=781,
        name="Dhelmise",
        types=('Ghost', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 131,
            "defense": 100,
            "speed": 40,
            "special": 86
        }),
        moves=('swords dance', 'slam', 'wrap', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=782,
        name="Jangmo-o",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 55,
            "defense": 65,
            "speed": 45,
            "special": 45
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=783,
        name="Hakamo-o",
        types=('Dragon', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 75,
            "defense": 90,
            "speed": 65,
            "special": 65
        }),
        moves=('mega punch', 'swords dance', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=784,
        name="Kommo-o",
        types=('Dragon', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 110,
            "defense": 125,
            "speed": 85,
            "special": 100
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=785,
        name="Tapu-koko",
        types=('Electric', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 115,
            "defense": 85,
            "speed": 130,
            "special": 95
        }),
        moves=('thunder punch', 'fly', 'roar', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=786,
        name="Tapu-lele",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 75,
            "speed": 95,
            "special": 130
        }),
        moves=('psybeam', 'hyper beam', 'thunderbolt', 'thunder')
    ),
    PokemonBase(
        pokedex_number=787,
        name="Tapu-bulu",
        types=('Grass', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 130,
            "defense": 115,
            "speed": 75,
            "special": 85
        }),
        moves=('mega punch', 'swords dance', 'whirlwind', 'horn attack')
    ),
    PokemonBase(
        pokedex_number=788,
        name="Tapu-fini",
        types=('Water', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 75,
            "defense": 115,
            "speed": 85,
            "special": 95
        }),
        moves=('ice punch', 'mist', 'water gun', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=789,
        name="Cosmog",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 43,
            "attack": 29,
            "defense": 31,
            "speed": 37,
            "special": 29
        }),
        moves=('teleport', 'splash')
    ),
    PokemonBase(
        pokedex_number=790,
        name="Cosmoem",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 43,
            "attack": 29,
            "defense": 131,
            "speed": 37,
            "special": 29
        }),
        moves=('teleport', 'cosmic power')
    ),
    PokemonBase(
        pokedex_number=791,
        name="Solgaleo",
        types=('Psychic', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 137,
            "attack": 137,
            "defense": 107,
            "speed": 97,
            "special": 113
        }),
        moves=('body slam', 'take down', 'double edge', 'roar')
    ),
    PokemonBase(
        pokedex_number=792,
        name="Lunala",
        types=('Psychic', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 137,
            "attack": 113,
            "defense": 89,
            "speed": 97,
            "special": 137
        }),
        moves=('fly', 'roar', 'ice beam', 'blizzard')
    ),
    PokemonBase(
        pokedex_number=793,
        name="Nihilego",
        types=('Rock', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 109,
            "attack": 53,
            "defense": 47,
            "speed": 103,
            "special": 127
        }),
        moves=('pound', 'bind', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=794,
        name="Buzzwole",
        types=('Bug', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 107,
            "attack": 139,
            "defense": 139,
            "speed": 79,
            "special": 53
        }),
        moves=('comet punch', 'mega punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=795,
        name="Pheromosa",
        types=('Bug', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 137,
            "defense": 37,
            "speed": 151,
            "special": 137
        }),
        moves=('stomp', 'double kick', 'jump kick', 'leer')
    ),
    PokemonBase(
        pokedex_number=796,
        name="Xurkitree",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 83,
            "attack": 89,
            "defense": 71,
            "speed": 83,
            "special": 173
        }),
        moves=('thunder punch', 'bind', 'wrap', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=797,
        name="Celesteela",
        types=('Steel', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 97,
            "attack": 101,
            "defense": 103,
            "speed": 61,
            "special": 107
        }),
        moves=('fly', 'tackle', 'body slam', 'double edge')
    ),
    PokemonBase(
        pokedex_number=798,
        name="Kartana",
        types=('Grass', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 181,
            "defense": 131,
            "speed": 109,
            "special": 59
        }),
        moves=('guillotine', 'swords dance', 'cut', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=799,
        name="Guzzlord",
        types=('Dark', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 223,
            "attack": 101,
            "defense": 53,
            "speed": 43,
            "special": 97
        }),
        moves=('mega punch', 'stomp', 'mega kick', 'body slam')
    ),
    PokemonBase(
        pokedex_number=800,
        name="Necrozma",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 97,
            "attack": 107,
            "defense": 101,
            "speed": 79,
            "special": 127
        }),
        moves=('swords dance', 'body slam', 'hyper beam', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=801,
        name="Magearna",
        types=('Steel', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 95,
            "defense": 115,
            "speed": 65,
            "special": 130
        }),
        moves=('body slam', 'take down', 'sonic boom', 'ice beam')
    ),
    PokemonBase(
        pokedex_number=802,
        name="Marshadow",
        types=('Fighting', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 125,
            "defense": 80,
            "speed": 125,
            "special": 90
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=803,
        name="Poipole",
        types=('Poison',),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 73,
            "defense": 67,
            "speed": 73,
            "special": 73
        }),
        moves=('fury attack', 'pin missile', 'growl', 'acid')
    ),
    PokemonBase(
        pokedex_number=804,
        name="Naganadel",
        types=('Poison', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 73,
            "attack": 73,
            "defense": 73,
            "speed": 121,
            "special": 127
        }),
        moves=('fly', 'fury attack', 'pin missile', 'growl')
    ),
    PokemonBase(
        pokedex_number=805,
        name="Stakataka",
        types=('Rock', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 131,
            "defense": 211,
            "speed": 13,
            "special": 53
        }),
        moves=('bind', 'stomp', 'mega kick', 'tackle')
    ),
    PokemonBase(
        pokedex_number=806,
        name="Blacephalon",
        types=('Fire', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 53,
            "attack": 127,
            "defense": 53,
            "speed": 107,
            "special": 151
        }),
        moves=('fire punch', 'ember', 'flamethrower', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=807,
        name="Zeraora",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 112,
            "defense": 75,
            "speed": 143,
            "special": 102
        }),
        moves=('mega punch', 'pay day', 'fire punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=808,
        name="Meltan",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 46,
            "attack": 65,
            "defense": 65,
            "speed": 34,
            "special": 55
        }),
        moves=('headbutt', 'tail whip', 'thunder shock', 'thunderbolt')
    ),
    PokemonBase(
        pokedex_number=809,
        name="Melmetal",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 135,
            "attack": 143,
            "defense": 143,
            "speed": 34,
            "special": 80
        }),
        moves=('mega punch', 'ice punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=810,
        name="Grookey",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 50,
            "speed": 65,
            "special": 40
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'slam')
    ),
    PokemonBase(
        pokedex_number=811,
        name="Thwackey",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 70,
            "speed": 80,
            "special": 55
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'slam')
    ),
    PokemonBase(
        pokedex_number=812,
        name="Rillaboom",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 125,
            "defense": 90,
            "speed": 85,
            "special": 60
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'slam')
    ),
    PokemonBase(
        pokedex_number=813,
        name="Scorbunny",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 71,
            "defense": 40,
            "speed": 69,
            "special": 40
        }),
        moves=('double kick', 'mega kick', 'sand attack', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=814,
        name="Raboot",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 86,
            "defense": 60,
            "speed": 94,
            "special": 55
        }),
        moves=('swords dance', 'double kick', 'mega kick', 'sand attack')
    ),
    PokemonBase(
        pokedex_number=815,
        name="Cinderace",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 116,
            "defense": 75,
            "speed": 119,
            "special": 65
        }),
        moves=('fire punch', 'swords dance', 'double kick', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=816,
        name="Sobble",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 40,
            "defense": 40,
            "speed": 70,
            "special": 70
        }),
        moves=('pound', 'bind', 'take down', 'growl')
    ),
    PokemonBase(
        pokedex_number=817,
        name="Drizzile",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 60,
            "defense": 55,
            "speed": 90,
            "special": 95
        }),
        moves=('pound', 'bind', 'take down', 'growl')
    ),
    PokemonBase(
        pokedex_number=818,
        name="Inteleon",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 65,
            "speed": 120,
            "special": 125
        }),
        moves=('pound', 'swords dance', 'bind', 'take down')
    ),
    PokemonBase(
        pokedex_number=819,
        name="Skwovet",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 55,
            "defense": 55,
            "speed": 25,
            "special": 35
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=820,
        name="Greedent",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 95,
            "defense": 95,
            "speed": 20,
            "special": 55
        }),
        moves=('swords dance', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=821,
        name="Rookidee",
        types=('Flying',),
        base_stats=MappingProxyType({
            "hp": 38,
            "attack": 47,
            "defense": 35,
            "speed": 57,
            "special": 33
        }),
        moves=('fly', 'sand attack', 'fury attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=822,
        name="Corvisquire",
        types=('Flying',),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 67,
            "defense": 55,
            "speed": 77,
            "special": 43
        }),
        moves=('fly', 'fury attack', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=823,
        name="Corviknight",
        types=('Flying', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 98,
            "attack": 87,
            "defense": 105,
            "speed": 67,
            "special": 53
        }),
        moves=('fly', 'sand attack', 'fury attack', 'body slam')
    ),
    PokemonBase(
        pokedex_number=824,
        name="Blipbug",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 25,
            "attack": 20,
            "defense": 20,
            "speed": 45,
            "special": 25
        }),
        moves=('supersonic', 'recover', 'struggle bug', 'sticky web')
    ),
    PokemonBase(
        pokedex_number=825,
        name="Dottler",
        types=('Bug', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 35,
            "defense": 80,
            "speed": 30,
            "special": 50
        }),
        moves=('solar beam', 'confusion', 'psychic', 'light screen')
    ),
    PokemonBase(
        pokedex_number=826,
        name="Orbeetle",
        types=('Bug', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 110,
            "speed": 90,
            "special": 80
        }),
        moves=('psybeam', 'hyper beam', 'solar beam', 'confusion')
    ),
    PokemonBase(
        pokedex_number=827,
        name="Nickit",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 28,
            "defense": 28,
            "speed": 50,
            "special": 47
        }),
        moves=('tail whip', 'dig', 'agility', 'quick attack')
    ),
    PokemonBase(
        pokedex_number=828,
        name="Thievul",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 58,
            "defense": 58,
            "speed": 90,
            "special": 87
        }),
        moves=('tail whip', 'hyper beam', 'dig', 'psychic')
    ),
    PokemonBase(
        pokedex_number=829,
        name="Gossifleur",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 60,
            "speed": 10,
            "special": 40
        }),
        moves=('sing', 'leech seed', 'growth', 'razor leaf')
    ),
    PokemonBase(
        pokedex_number=830,
        name="Eldegoss",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 50,
            "defense": 90,
            "speed": 60,
            "special": 80
        }),
        moves=('sing', 'hyper beam', 'razor leaf', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=831,
        name="Wooloo",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 42,
            "attack": 40,
            "defense": 55,
            "speed": 48,
            "special": 40
        }),
        moves=('stomp', 'double kick', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=832,
        name="Dubwool",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 80,
            "defense": 100,
            "speed": 88,
            "special": 60
        }),
        moves=('swords dance', 'double kick', 'mega kick', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=833,
        name="Chewtle",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 64,
            "defense": 50,
            "speed": 44,
            "special": 38
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=834,
        name="Drednaw",
        types=('Water', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 115,
            "defense": 90,
            "speed": 74,
            "special": 48
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=835,
        name="Yamper",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 59,
            "attack": 45,
            "defense": 50,
            "speed": 26,
            "special": 40
        }),
        moves=('sand attack', 'tackle', 'double edge', 'tail whip')
    ),
    PokemonBase(
        pokedex_number=836,
        name="Boltund",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 69,
            "attack": 90,
            "defense": 60,
            "speed": 121,
            "special": 90
        }),
        moves=('tackle', 'tail whip', 'bite', 'roar')
    ),
    PokemonBase(
        pokedex_number=837,
        name="Rolycoly",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 40,
            "defense": 50,
            "speed": 30,
            "special": 40
        }),
        moves=('tackle', 'body slam', 'take down', 'dig')
    ),
    PokemonBase(
        pokedex_number=838,
        name="Carkol",
        types=('Rock', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 60,
            "defense": 90,
            "speed": 50,
            "special": 60
        }),
        moves=('tackle', 'body slam', 'take down', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=839,
        name="Coalossal",
        types=('Rock', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 80,
            "defense": 120,
            "speed": 30,
            "special": 80
        }),
        moves=('mega punch', 'fire punch', 'mega kick', 'tackle')
    ),
    PokemonBase(
        pokedex_number=840,
        name="Applin",
        types=('Grass', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 80,
            "speed": 20,
            "special": 40
        }),
        moves=('withdraw', 'defense curl', 'rollout', 'attract')
    ),
    PokemonBase(
        pokedex_number=841,
        name="Flapple",
        types=('Grass', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 110,
            "defense": 80,
            "speed": 70,
            "special": 95
        }),
        moves=('wing attack', 'fly', 'take down', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=842,
        name="Appletun",
        types=('Grass', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 85,
            "defense": 80,
            "speed": 30,
            "special": 100
        }),
        moves=('stomp', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=843,
        name="Silicobra",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 52,
            "attack": 57,
            "defense": 75,
            "speed": 46,
            "special": 35
        }),
        moves=('slam', 'sand attack', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=844,
        name="Sandaconda",
        types=('Ground',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 107,
            "defense": 125,
            "speed": 71,
            "special": 65
        }),
        moves=('slam', 'sand attack', 'headbutt', 'body slam')
    ),
    PokemonBase(
        pokedex_number=845,
        name="Cramorant",
        types=('Flying', 'Water'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 55,
            "speed": 85,
            "special": 85
        }),
        moves=('fly', 'fury attack', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=846,
        name="Arrokuda",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 63,
            "defense": 40,
            "speed": 66,
            "special": 40
        }),
        moves=('fury attack', 'take down', 'thrash', 'double edge')
    ),
    PokemonBase(
        pokedex_number=847,
        name="Barraskewda",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 123,
            "defense": 60,
            "speed": 136,
            "special": 60
        }),
        moves=('fury attack', 'take down', 'double edge', 'bite')
    ),
    PokemonBase(
        pokedex_number=848,
        name="Toxel",
        types=('Electric', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 38,
            "defense": 35,
            "speed": 40,
            "special": 54
        }),
        moves=('growl', 'acid', 'rest', 'substitute')
    ),
    PokemonBase(
        pokedex_number=849,
        name="Toxtricity-amped",
        types=('Electric', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 98,
            "defense": 70,
            "speed": 75,
            "special": 114
        }),
        moves=('mega punch', 'fire punch', 'thunder punch', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=850,
        name="Sizzlipede",
        types=('Fire', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 65,
            "defense": 45,
            "speed": 45,
            "special": 50
        }),
        moves=('slam', 'wrap', 'bite', 'ember')
    ),
    PokemonBase(
        pokedex_number=851,
        name="Centiskorch",
        types=('Fire', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 115,
            "defense": 65,
            "speed": 65,
            "special": 90
        }),
        moves=('slam', 'wrap', 'bite', 'ember')
    ),
    PokemonBase(
        pokedex_number=852,
        name="Clobbopus",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 68,
            "defense": 60,
            "speed": 32,
            "special": 50
        }),
        moves=('mega punch', 'ice punch', 'bind', 'body slam')
    ),
    PokemonBase(
        pokedex_number=853,
        name="Grapploct",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 118,
            "defense": 90,
            "speed": 42,
            "special": 70
        }),
        moves=('mega punch', 'ice punch', 'bind', 'body slam')
    ),
    PokemonBase(
        pokedex_number=854,
        name="Sinistea",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 45,
            "speed": 50,
            "special": 74
        }),
        moves=('psybeam', 'mega drain', 'psychic', 'night shade')
    ),
    PokemonBase(
        pokedex_number=855,
        name="Polteageist",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 65,
            "defense": 65,
            "speed": 70,
            "special": 134
        }),
        moves=('psybeam', 'hyper beam', 'mega drain', 'psychic')
    ),
    PokemonBase(
        pokedex_number=856,
        name="Hatenna",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 42,
            "attack": 30,
            "defense": 45,
            "speed": 39,
            "special": 56
        }),
        moves=('psybeam', 'thunder wave', 'confusion', 'psychic')
    ),
    PokemonBase(
        pokedex_number=857,
        name="Hattrem",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 40,
            "defense": 65,
            "speed": 49,
            "special": 86
        }),
        moves=('psybeam', 'thunder wave', 'confusion', 'psychic')
    ),
    PokemonBase(
        pokedex_number=858,
        name="Hatterene",
        types=('Psychic', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 90,
            "defense": 95,
            "speed": 29,
            "special": 136
        }),
        moves=('swords dance', 'psybeam', 'hyper beam', 'thunder wave')
    ),
    PokemonBase(
        pokedex_number=859,
        name="Impidimp",
        types=('Dark', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 45,
            "defense": 30,
            "speed": 50,
            "special": 55
        }),
        moves=('mega punch', 'mega kick', 'take down', 'bite')
    ),
    PokemonBase(
        pokedex_number=860,
        name="Morgrem",
        types=('Dark', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 60,
            "defense": 45,
            "speed": 70,
            "special": 75
        }),
        moves=('mega punch', 'mega kick', 'take down', 'bite')
    ),
    PokemonBase(
        pokedex_number=861,
        name="Grimmsnarl",
        types=('Dark', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 120,
            "defense": 65,
            "speed": 60,
            "special": 95
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=862,
        name="Obstagoon",
        types=('Dark', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 93,
            "attack": 90,
            "defense": 101,
            "speed": 95,
            "special": 60
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=863,
        name="Perrserker",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 110,
            "defense": 100,
            "speed": 50,
            "special": 50
        }),
        moves=('pay day', 'scratch', 'swords dance', 'body slam')
    ),
    PokemonBase(
        pokedex_number=864,
        name="Cursola",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 95,
            "defense": 50,
            "speed": 30,
            "special": 145
        }),
        moves=('tackle', 'body slam', 'pin missile', 'disable')
    ),
    PokemonBase(
        pokedex_number=865,
        name="Sirfetchd",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 62,
            "attack": 135,
            "defense": 95,
            "speed": 65,
            "special": 68
        }),
        moves=('swords dance', 'slam', 'sand attack', 'body slam')
    ),
    PokemonBase(
        pokedex_number=866,
        name="Mr-rime",
        types=('Ice', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 85,
            "defense": 75,
            "speed": 70,
            "special": 110
        }),
        moves=('pound', 'mega punch', 'ice punch', 'double kick')
    ),
    PokemonBase(
        pokedex_number=867,
        name="Runerigus",
        types=('Ground', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 95,
            "defense": 145,
            "speed": 30,
            "special": 50
        }),
        moves=('slam', 'disable', 'hyper beam', 'earthquake')
    ),
    PokemonBase(
        pokedex_number=868,
        name="Milcery",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 40,
            "defense": 40,
            "speed": 34,
            "special": 50
        }),
        moves=('tackle', 'recover', 'acid armor', 'rest')
    ),
    PokemonBase(
        pokedex_number=869,
        name="Alcremie",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 60,
            "defense": 75,
            "speed": 64,
            "special": 110
        }),
        moves=('tackle', 'hyper beam', 'solar beam', 'psychic')
    ),
    PokemonBase(
        pokedex_number=870,
        name="Falinks",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 100,
            "defense": 100,
            "speed": 75,
            "special": 70
        }),
        moves=('swords dance', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=871,
        name="Pincurchin",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 101,
            "defense": 95,
            "speed": 15,
            "special": 91
        }),
        moves=('fury attack', 'body slam', 'take down', 'pin missile')
    ),
    PokemonBase(
        pokedex_number=872,
        name="Snom",
        types=('Ice', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 25,
            "defense": 35,
            "speed": 20,
            "special": 45
        }),
        moves=('rest', 'substitute', 'snore', 'powder snow')
    ),
    PokemonBase(
        pokedex_number=873,
        name="Frosmoth",
        types=('Ice', 'Bug'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 65,
            "defense": 60,
            "speed": 65,
            "special": 125
        }),
        moves=('take down', 'mist', 'ice beam', 'blizzard')
    ),
    PokemonBase(
        pokedex_number=874,
        name="Stonjourner",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 125,
            "defense": 135,
            "speed": 70,
            "special": 20
        }),
        moves=('stomp', 'mega kick', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=875,
        name="Eiscue-ice",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 80,
            "defense": 110,
            "speed": 50,
            "special": 65
        }),
        moves=('ice punch', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=876,
        name="Indeedee-male",
        types=('Psychic', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 65,
            "defense": 55,
            "speed": 95,
            "special": 105
        }),
        moves=('pay day', 'body slam', 'take down', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=877,
        name="Morpeko-full-belly",
        types=('Electric', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 58,
            "attack": 95,
            "defense": 58,
            "speed": 97,
            "special": 70
        }),
        moves=('thunder punch', 'take down', 'thrash', 'double edge')
    ),
    PokemonBase(
        pokedex_number=878,
        name="Cufant",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 80,
            "defense": 49,
            "speed": 40,
            "special": 40
        }),
        moves=('whirlwind', 'slam', 'stomp', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=879,
        name="Copperajah",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 122,
            "attack": 130,
            "defense": 69,
            "speed": 30,
            "special": 80
        }),
        moves=('stomp', 'mega kick', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=880,
        name="Dracozolt",
        types=('Electric', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 100,
            "defense": 90,
            "speed": 75,
            "special": 80
        }),
        moves=('mega punch', 'thunder punch', 'slam', 'stomp')
    ),
    PokemonBase(
        pokedex_number=881,
        name="Arctozolt",
        types=('Electric', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 100,
            "defense": 90,
            "speed": 55,
            "special": 90
        }),
        moves=('mega punch', 'thunder punch', 'slam', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=882,
        name="Dracovish",
        types=('Water', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 90,
            "defense": 100,
            "speed": 75,
            "special": 70
        }),
        moves=('stomp', 'mega kick', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=883,
        name="Arctovish",
        types=('Water', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 90,
            "defense": 100,
            "speed": 55,
            "special": 80
        }),
        moves=('body slam', 'bite', 'water gun', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=884,
        name="Duraludon",
        types=('Steel', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 95,
            "defense": 115,
            "speed": 85,
            "special": 120
        }),
        moves=('swords dance', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=885,
        name="Dreepy",
        types=('Dragon', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 28,
            "attack": 60,
            "defense": 30,
            "speed": 82,
            "special": 40
        }),
        moves=('bite', 'disable', 'thunder wave', 'quick attack')
    ),
    PokemonBase(
        pokedex_number=886,
        name="Drakloak",
        types=('Dragon', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 80,
            "defense": 50,
            "speed": 102,
            "special": 60
        }),
        moves=('take down', 'double edge', 'bite', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=887,
        name="Dragapult",
        types=('Dragon', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 120,
            "defense": 75,
            "speed": 142,
            "special": 100
        }),
        moves=('fly', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=888,
        name="Zacian",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 92,
            "attack": 120,
            "defense": 115,
            "speed": 138,
            "special": 80
        }),
        moves=('swords dance', 'body slam', 'take down', 'bite')
    ),
    PokemonBase(
        pokedex_number=889,
        name="Zamazenta",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 92,
            "attack": 120,
            "defense": 115,
            "speed": 138,
            "special": 80
        }),
        moves=('body slam', 'take down', 'bite', 'roar')
    ),
    PokemonBase(
        pokedex_number=890,
        name="Eternatus",
        types=('Poison', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 140,
            "attack": 85,
            "defense": 95,
            "speed": 130,
            "special": 145
        }),
        moves=('fly', 'body slam', 'take down', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=891,
        name="Kubfu",
        types=('Fighting',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 90,
            "defense": 60,
            "speed": 72,
            "special": 53
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=892,
        name="Urshifu-single-strike",
        types=('Fighting', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 130,
            "defense": 100,
            "speed": 97,
            "special": 63
        }),
        moves=('mega punch', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=893,
        name="Zarude",
        types=('Dark', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 120,
            "defense": 105,
            "speed": 105,
            "special": 70
        }),
        moves=('mega punch', 'scratch', 'swords dance', 'bind')
    ),
    PokemonBase(
        pokedex_number=894,
        name="Regieleki",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 100,
            "defense": 50,
            "speed": 200,
            "special": 100
        }),
        moves=('body slam', 'take down', 'thrash', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=895,
        name="Regidrago",
        types=('Dragon',),
        base_stats=MappingProxyType({
            "hp": 200,
            "attack": 100,
            "defense": 50,
            "speed": 80,
            "special": 100
        }),
        moves=('vice grip', 'body slam', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=896,
        name="Glastrier",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 145,
            "defense": 130,
            "speed": 30,
            "special": 65
        }),
        moves=('swords dance', 'stomp', 'double kick', 'tackle')
    ),
    PokemonBase(
        pokedex_number=897,
        name="Spectrier",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 65,
            "defense": 60,
            "speed": 130,
            "special": 145
        }),
        moves=('stomp', 'double kick', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=898,
        name="Calyrex",
        types=('Psychic', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 80,
            "defense": 80,
            "speed": 80,
            "special": 80
        }),
        moves=('pound', 'pay day', 'take down', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=899,
        name="Wyrdeer",
        types=('Normal', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 103,
            "attack": 105,
            "defense": 72,
            "speed": 65,
            "special": 105
        }),
        moves=('stomp', 'sand attack', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=900,
        name="Kleavor",
        types=('Bug', 'Rock'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 135,
            "defense": 95,
            "speed": 85,
            "special": 45
        }),
        moves=('swords dance', 'take down', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=901,
        name="Ursaluna",
        types=('Ground', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 130,
            "attack": 140,
            "defense": 105,
            "speed": 50,
            "special": 45
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=902,
        name="Basculegion-male",
        types=('Water', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 112,
            "defense": 65,
            "speed": 78,
            "special": 80
        }),
        moves=('headbutt', 'tackle', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=903,
        name="Sneasler",
        types=('Fighting', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 130,
            "defense": 60,
            "speed": 120,
            "special": 40
        }),
        moves=('fire punch', 'scratch', 'swords dance', 'take down')
    ),
    PokemonBase(
        pokedex_number=904,
        name="Overqwil",
        types=('Dark', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 115,
            "defense": 95,
            "speed": 85,
            "special": 65
        }),
        moves=('swords dance', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=905,
        name="Enamorus-incarnate",
        types=('Fairy', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 115,
            "defense": 70,
            "speed": 106,
            "special": 135
        }),
        moves=('fly', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=906,
        name="Sprigatito",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 61,
            "defense": 54,
            "speed": 65,
            "special": 45
        }),
        moves=('scratch', 'take down', 'tail whip', 'bite')
    ),
    PokemonBase(
        pokedex_number=907,
        name="Floragato",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 80,
            "defense": 63,
            "speed": 83,
            "special": 60
        }),
        moves=('thunder punch', 'scratch', 'take down', 'tail whip')
    ),
    PokemonBase(
        pokedex_number=908,
        name="Meowscarada",
        types=('Grass', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 76,
            "attack": 110,
            "defense": 70,
            "speed": 123,
            "special": 81
        }),
        moves=('thunder punch', 'scratch', 'take down', 'tail whip')
    ),
    PokemonBase(
        pokedex_number=909,
        name="Fuecoco",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 67,
            "attack": 45,
            "defense": 59,
            "speed": 36,
            "special": 63
        }),
        moves=('tackle', 'body slam', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=910,
        name="Crocalor",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 81,
            "attack": 55,
            "defense": 78,
            "speed": 49,
            "special": 90
        }),
        moves=('tackle', 'body slam', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=911,
        name="Skeledirge",
        types=('Fire', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 104,
            "attack": 75,
            "defense": 100,
            "speed": 66,
            "special": 110
        }),
        moves=('tackle', 'body slam', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=912,
        name="Quaxly",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 65,
            "defense": 45,
            "speed": 50,
            "special": 50
        }),
        moves=('pound', 'wing attack', 'take down', 'growl')
    ),
    PokemonBase(
        pokedex_number=913,
        name="Quaxwell",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 65,
            "speed": 65,
            "special": 65
        }),
        moves=('pound', 'wing attack', 'take down', 'growl')
    ),
    PokemonBase(
        pokedex_number=914,
        name="Quaquaval",
        types=('Water', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 120,
            "defense": 80,
            "speed": 85,
            "special": 85
        }),
        moves=('pound', 'swords dance', 'wing attack', 'mega kick')
    ),
    PokemonBase(
        pokedex_number=915,
        name="Lechonk",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 54,
            "attack": 45,
            "defense": 40,
            "speed": 35,
            "special": 35
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=916,
        name="Oinkologne-male",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 100,
            "defense": 75,
            "speed": 65,
            "special": 59
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=917,
        name="Tarountula",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 41,
            "defense": 45,
            "speed": 20,
            "special": 29
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=918,
        name="Spidops",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 79,
            "defense": 92,
            "speed": 35,
            "special": 52
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=919,
        name="Nymble",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 33,
            "attack": 46,
            "defense": 40,
            "speed": 45,
            "special": 21
        }),
        moves=('double kick', 'tackle', 'take down', 'leer')
    ),
    PokemonBase(
        pokedex_number=920,
        name="Lokix",
        types=('Bug', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 102,
            "defense": 78,
            "speed": 92,
            "special": 52
        }),
        moves=('swords dance', 'double kick', 'tackle', 'take down')
    ),
    PokemonBase(
        pokedex_number=921,
        name="Pawmi",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 50,
            "defense": 20,
            "speed": 60,
            "special": 40
        }),
        moves=('scratch', 'slam', 'take down', 'bite')
    ),
    PokemonBase(
        pokedex_number=922,
        name="Pawmo",
        types=('Electric', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 75,
            "defense": 40,
            "speed": 85,
            "special": 50
        }),
        moves=('thunder punch', 'scratch', 'slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=923,
        name="Pawmot",
        types=('Electric', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 115,
            "defense": 70,
            "speed": 105,
            "special": 70
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=924,
        name="Tandemaus",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 50,
            "defense": 45,
            "speed": 75,
            "special": 40
        }),
        moves=('pound', 'take down', 'double edge', 'bite')
    ),
    PokemonBase(
        pokedex_number=925,
        name="Maushold-family-of-four",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 75,
            "defense": 70,
            "speed": 111,
            "special": 65
        }),
        moves=('pound', 'take down', 'double edge', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=926,
        name="Fidough",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 37,
            "attack": 55,
            "defense": 70,
            "speed": 65,
            "special": 30
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=927,
        name="Dachsbun",
        types=('Fairy',),
        base_stats=MappingProxyType({
            "hp": 57,
            "attack": 80,
            "defense": 115,
            "speed": 95,
            "special": 50
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=928,
        name="Smoliv",
        types=('Grass', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 35,
            "defense": 45,
            "speed": 30,
            "special": 58
        }),
        moves=('tackle', 'absorb', 'mega drain', 'leech seed')
    ),
    PokemonBase(
        pokedex_number=929,
        name="Dolliv",
        types=('Grass', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 52,
            "attack": 53,
            "defense": 60,
            "speed": 33,
            "special": 78
        }),
        moves=('tackle', 'absorb', 'mega drain', 'leech seed')
    ),
    PokemonBase(
        pokedex_number=930,
        name="Arboliva",
        types=('Grass', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 78,
            "attack": 69,
            "defense": 90,
            "speed": 39,
            "special": 125
        }),
        moves=('tackle', 'hyper beam', 'absorb', 'mega drain')
    ),
    PokemonBase(
        pokedex_number=931,
        name="Squawkabilly-green-plumage",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 82,
            "attack": 96,
            "defense": 51,
            "speed": 92,
            "special": 45
        }),
        moves=('fly', 'fury attack', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=932,
        name="Nacli",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 75,
            "speed": 25,
            "special": 35
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=933,
        name="Naclstack",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 60,
            "defense": 100,
            "speed": 35,
            "special": 35
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=934,
        name="Garganacl",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 100,
            "defense": 130,
            "speed": 35,
            "special": 45
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=935,
        name="Charcadet",
        types=('Fire',),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 50,
            "defense": 40,
            "speed": 35,
            "special": 50
        }),
        moves=('take down', 'leer', 'disable', 'ember')
    ),
    PokemonBase(
        pokedex_number=936,
        name="Armarouge",
        types=('Fire', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 60,
            "defense": 100,
            "speed": 75,
            "special": 125
        }),
        moves=('take down', 'leer', 'ember', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=937,
        name="Ceruledge",
        types=('Fire', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 125,
            "defense": 80,
            "speed": 85,
            "special": 60
        }),
        moves=('swords dance', 'take down', 'leer', 'ember')
    ),
    PokemonBase(
        pokedex_number=938,
        name="Tadbulb",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 61,
            "attack": 31,
            "defense": 41,
            "speed": 45,
            "special": 59
        }),
        moves=('tackle', 'water gun', 'thunder shock', 'thunderbolt')
    ),
    PokemonBase(
        pokedex_number=939,
        name="Bellibolt",
        types=('Electric',),
        base_stats=MappingProxyType({
            "hp": 109,
            "attack": 64,
            "defense": 91,
            "speed": 45,
            "special": 103
        }),
        moves=('tackle', 'water gun', 'hyper beam', 'thunder shock')
    ),
    PokemonBase(
        pokedex_number=940,
        name="Wattrel",
        types=('Electric', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 35,
            "speed": 70,
            "special": 55
        }),
        moves=('fly', 'take down', 'growl', 'peck')
    ),
    PokemonBase(
        pokedex_number=941,
        name="Kilowattrel",
        types=('Electric', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 70,
            "defense": 60,
            "speed": 125,
            "special": 105
        }),
        moves=('fly', 'take down', 'growl', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=942,
        name="Maschiff",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 78,
            "defense": 60,
            "speed": 51,
            "special": 40
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=943,
        name="Mabosstiff",
        types=('Dark',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 90,
            "speed": 85,
            "special": 60
        }),
        moves=('headbutt', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=944,
        name="Shroodle",
        types=('Poison', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 65,
            "defense": 35,
            "speed": 75,
            "special": 40
        }),
        moves=('scratch', 'swords dance', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=945,
        name="Grafaiai",
        types=('Poison', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 63,
            "attack": 95,
            "defense": 65,
            "speed": 110,
            "special": 80
        }),
        moves=('scratch', 'swords dance', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=946,
        name="Bramblin",
        types=('Grass', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 65,
            "defense": 30,
            "speed": 60,
            "special": 45
        }),
        moves=('disable', 'absorb', 'mega drain', 'leech seed')
    ),
    PokemonBase(
        pokedex_number=947,
        name="Brambleghast",
        types=('Grass', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 115,
            "defense": 70,
            "speed": 90,
            "special": 80
        }),
        moves=('disable', 'hyper beam', 'absorb', 'mega drain')
    ),
    PokemonBase(
        pokedex_number=948,
        name="Toedscool",
        types=('Ground', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 40,
            "defense": 35,
            "speed": 70,
            "special": 50
        }),
        moves=('tackle', 'wrap', 'supersonic', 'absorb')
    ),
    PokemonBase(
        pokedex_number=949,
        name="Toedscruel",
        types=('Ground', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 70,
            "defense": 65,
            "speed": 100,
            "special": 80
        }),
        moves=('tackle', 'wrap', 'supersonic', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=950,
        name="Klawf",
        types=('Rock',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 100,
            "defense": 115,
            "speed": 75,
            "special": 35
        }),
        moves=('guillotine', 'swords dance', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=951,
        name="Capsakid",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 62,
            "defense": 40,
            "speed": 50,
            "special": 62
        }),
        moves=('headbutt', 'take down', 'leer', 'bite')
    ),
    PokemonBase(
        pokedex_number=952,
        name="Scovillain",
        types=('Grass', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 108,
            "defense": 65,
            "speed": 75,
            "special": 108
        }),
        moves=('headbutt', 'take down', 'leer', 'bite')
    ),
    PokemonBase(
        pokedex_number=953,
        name="Rellor",
        types=('Bug',),
        base_stats=MappingProxyType({
            "hp": 41,
            "attack": 50,
            "defense": 60,
            "speed": 30,
            "special": 31
        }),
        moves=('sand attack', 'tackle', 'take down', 'dig')
    ),
    PokemonBase(
        pokedex_number=954,
        name="Rabsca",
        types=('Bug', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 75,
            "attack": 50,
            "defense": 85,
            "speed": 45,
            "special": 115
        }),
        moves=('sand attack', 'tackle', 'take down', 'psybeam')
    ),
    PokemonBase(
        pokedex_number=955,
        name="Flittle",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 30,
            "attack": 35,
            "defense": 30,
            "speed": 75,
            "special": 55
        }),
        moves=('take down', 'growl', 'psybeam', 'peck')
    ),
    PokemonBase(
        pokedex_number=956,
        name="Espathra",
        types=('Psychic',),
        base_stats=MappingProxyType({
            "hp": 95,
            "attack": 60,
            "defense": 60,
            "speed": 105,
            "special": 101
        }),
        moves=('body slam', 'take down', 'double edge', 'growl')
    ),
    PokemonBase(
        pokedex_number=957,
        name="Tinkatink",
        types=('Fairy', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 45,
            "defense": 45,
            "speed": 58,
            "special": 35
        }),
        moves=('swords dance', 'slam', 'thunder wave', 'light screen')
    ),
    PokemonBase(
        pokedex_number=958,
        name="Tinkatuff",
        types=('Fairy', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 55,
            "defense": 55,
            "speed": 78,
            "special": 45
        }),
        moves=('swords dance', 'slam', 'thunder wave', 'light screen')
    ),
    PokemonBase(
        pokedex_number=959,
        name="Tinkaton",
        types=('Fairy', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 75,
            "defense": 77,
            "speed": 94,
            "special": 70
        }),
        moves=('swords dance', 'slam', 'thunder wave', 'light screen')
    ),
    PokemonBase(
        pokedex_number=960,
        name="Wiglett",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 10,
            "attack": 55,
            "defense": 25,
            "speed": 95,
            "special": 35
        }),
        moves=('slam', 'sand attack', 'headbutt', 'wrap')
    ),
    PokemonBase(
        pokedex_number=961,
        name="Wugtrio",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 35,
            "attack": 100,
            "defense": 50,
            "speed": 120,
            "special": 50
        }),
        moves=('slam', 'sand attack', 'headbutt', 'wrap')
    ),
    PokemonBase(
        pokedex_number=962,
        name="Bombirdier",
        types=('Flying', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 103,
            "defense": 85,
            "speed": 82,
            "special": 60
        }),
        moves=('wing attack', 'whirlwind', 'fly', 'take down')
    ),
    PokemonBase(
        pokedex_number=963,
        name="Finizen",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 45,
            "defense": 40,
            "speed": 75,
            "special": 45
        }),
        moves=('body slam', 'take down', 'supersonic', 'mist')
    ),
    PokemonBase(
        pokedex_number=964,
        name="Palafin-zero",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 70,
            "defense": 72,
            "speed": 100,
            "special": 53
        }),
        moves=('ice punch', 'body slam', 'take down', 'supersonic')
    ),
    PokemonBase(
        pokedex_number=965,
        name="Varoom",
        types=('Steel', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 70,
            "defense": 63,
            "speed": 47,
            "special": 30
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=966,
        name="Revavroom",
        types=('Steel', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 119,
            "defense": 90,
            "speed": 90,
            "special": 54
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=967,
        name="Cyclizar",
        types=('Dragon', 'Normal'),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 95,
            "defense": 65,
            "speed": 121,
            "special": 85
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=968,
        name="Orthworm",
        types=('Steel',),
        base_stats=MappingProxyType({
            "hp": 70,
            "attack": 85,
            "defense": 145,
            "speed": 65,
            "special": 60
        }),
        moves=('tackle', 'body slam', 'wrap', 'take down')
    ),
    PokemonBase(
        pokedex_number=969,
        name="Glimmet",
        types=('Rock', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 48,
            "attack": 35,
            "defense": 42,
            "speed": 60,
            "special": 105
        }),
        moves=('rock throw', 'toxic', 'harden', 'confuse ray')
    ),
    PokemonBase(
        pokedex_number=970,
        name="Glimmora",
        types=('Rock', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 83,
            "attack": 55,
            "defense": 90,
            "speed": 86,
            "special": 130
        }),
        moves=('hyper beam', 'solar beam', 'rock throw', 'toxic')
    ),
    PokemonBase(
        pokedex_number=971,
        name="Greavard",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 50,
            "attack": 61,
            "defense": 60,
            "speed": 34,
            "special": 30
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=972,
        name="Houndstone",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 72,
            "attack": 101,
            "defense": 100,
            "speed": 68,
            "special": 50
        }),
        moves=('headbutt', 'tackle', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=973,
        name="Flamigo",
        types=('Flying', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 82,
            "attack": 115,
            "defense": 74,
            "speed": 90,
            "special": 75
        }),
        moves=('swords dance', 'wing attack', 'fly', 'double kick')
    ),
    PokemonBase(
        pokedex_number=974,
        name="Cetoddle",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 108,
            "attack": 68,
            "defense": 45,
            "speed": 43,
            "special": 30
        }),
        moves=('tackle', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=975,
        name="Cetitan",
        types=('Ice',),
        base_stats=MappingProxyType({
            "hp": 170,
            "attack": 113,
            "defense": 65,
            "speed": 73,
            "special": 45
        }),
        moves=('ice punch', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=976,
        name="Veluza",
        types=('Water', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 102,
            "defense": 73,
            "speed": 70,
            "special": 78
        }),
        moves=('tackle', 'body slam', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=977,
        name="Dondozo",
        types=('Water',),
        base_stats=MappingProxyType({
            "hp": 150,
            "attack": 100,
            "defense": 115,
            "speed": 35,
            "special": 65
        }),
        moves=('tackle', 'body slam', 'take down', 'thrash')
    ),
    PokemonBase(
        pokedex_number=978,
        name="Tatsugiri-curly",
        types=('Dragon', 'Water'),
        base_stats=MappingProxyType({
            "hp": 68,
            "attack": 50,
            "defense": 60,
            "speed": 82,
            "special": 120
        }),
        moves=('take down', 'water gun', 'hydro pump', 'surf')
    ),
    PokemonBase(
        pokedex_number=979,
        name="Annihilape",
        types=('Fighting', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 110,
            "attack": 115,
            "defense": 80,
            "speed": 90,
            "special": 50
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'scratch')
    ),
    PokemonBase(
        pokedex_number=980,
        name="Clodsire",
        types=('Poison', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 130,
            "attack": 75,
            "defense": 60,
            "speed": 20,
            "special": 45
        }),
        moves=('slam', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=981,
        name="Farigiraf",
        types=('Normal', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 120,
            "attack": 90,
            "defense": 70,
            "speed": 60,
            "special": 110
        }),
        moves=('stomp', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=982,
        name="Dudunsparce-two-segment",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 125,
            "attack": 100,
            "defense": 80,
            "speed": 55,
            "special": 85
        }),
        moves=('body slam', 'take down', 'double edge', 'flamethrower')
    ),
    PokemonBase(
        pokedex_number=983,
        name="Kingambit",
        types=('Dark', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 135,
            "defense": 120,
            "speed": 50,
            "special": 60
        }),
        moves=('scratch', 'guillotine', 'swords dance', 'take down')
    ),
    PokemonBase(
        pokedex_number=984,
        name="Great-tusk",
        types=('Ground', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 131,
            "defense": 131,
            "speed": 87,
            "special": 53
        }),
        moves=('horn attack', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=985,
        name="Scream-tail",
        types=('Fairy', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 65,
            "defense": 99,
            "speed": 111,
            "special": 65
        }),
        moves=('pound', 'fire punch', 'ice punch', 'thunder punch')
    ),
    PokemonBase(
        pokedex_number=986,
        name="Brute-bonnet",
        types=('Grass', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 111,
            "attack": 127,
            "defense": 99,
            "speed": 55,
            "special": 79
        }),
        moves=('body slam', 'thrash', 'double edge', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=987,
        name="Flutter-mane",
        types=('Ghost', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 55,
            "defense": 55,
            "speed": 135,
            "special": 135
        }),
        moves=('psybeam', 'hyper beam', 'thunderbolt', 'thunder wave')
    ),
    PokemonBase(
        pokedex_number=988,
        name="Slither-wing",
        types=('Bug', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 135,
            "defense": 79,
            "speed": 81,
            "special": 85
        }),
        moves=('gust', 'whirlwind', 'stomp', 'body slam')
    ),
    PokemonBase(
        pokedex_number=989,
        name="Sandy-shocks",
        types=('Electric', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 81,
            "defense": 97,
            "speed": 101,
            "special": 121
        }),
        moves=('body slam', 'take down', 'supersonic', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=990,
        name="Iron-treads",
        types=('Ground', 'Steel'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 112,
            "defense": 120,
            "speed": 106,
            "special": 72
        }),
        moves=('horn attack', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=991,
        name="Iron-bundle",
        types=('Ice', 'Water'),
        base_stats=MappingProxyType({
            "hp": 56,
            "attack": 80,
            "defense": 114,
            "speed": 136,
            "special": 124
        }),
        moves=('ice punch', 'body slam', 'take down', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=992,
        name="Iron-hands",
        types=('Fighting', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 154,
            "attack": 140,
            "defense": 108,
            "speed": 50,
            "special": 50
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=993,
        name="Iron-jugulis",
        types=('Dark', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 94,
            "attack": 80,
            "defense": 86,
            "speed": 108,
            "special": 122
        }),
        moves=('fly', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=994,
        name="Iron-moth",
        types=('Fire', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 70,
            "defense": 60,
            "speed": 110,
            "special": 140
        }),
        moves=('gust', 'whirlwind', 'take down', 'ember')
    ),
    PokemonBase(
        pokedex_number=995,
        name="Iron-thorns",
        types=('Rock', 'Electric'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 134,
            "defense": 110,
            "speed": 72,
            "special": 70
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=996,
        name="Frigibax",
        types=('Dragon', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 75,
            "defense": 45,
            "speed": 55,
            "special": 35
        }),
        moves=('swords dance', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=997,
        name="Arctibax",
        types=('Dragon', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 95,
            "defense": 66,
            "speed": 62,
            "special": 45
        }),
        moves=('swords dance', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=998,
        name="Baxcalibur",
        types=('Dragon', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 115,
            "attack": 145,
            "defense": 92,
            "speed": 87,
            "special": 75
        }),
        moves=('swords dance', 'tackle', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=999,
        name="Gimmighoul",
        types=('Ghost',),
        base_stats=MappingProxyType({
            "hp": 45,
            "attack": 30,
            "defense": 70,
            "speed": 10,
            "special": 75
        }),
        moves=('tackle', 'take down', 'night shade', 'confuse ray')
    ),
    PokemonBase(
        pokedex_number=1000,
        name="Gholdengo",
        types=('Steel', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 87,
            "attack": 60,
            "defense": 95,
            "speed": 84,
            "special": 133
        }),
        moves=('thunder punch', 'tackle', 'take down', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=1001,
        name="Wo-chien",
        types=('Dark', 'Grass'),
        base_stats=MappingProxyType({
            "hp": 85,
            "attack": 85,
            "defense": 100,
            "speed": 70,
            "special": 95
        }),
        moves=('body slam', 'take down', 'hyper beam', 'absorb')
    ),
    PokemonBase(
        pokedex_number=1002,
        name="Chien-pao",
        types=('Dark', 'Ice'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 80,
            "speed": 135,
            "special": 90
        }),
        moves=('swords dance', 'take down', 'mist', 'blizzard')
    ),
    PokemonBase(
        pokedex_number=1003,
        name="Ting-lu",
        types=('Dark', 'Ground'),
        base_stats=MappingProxyType({
            "hp": 155,
            "attack": 110,
            "defense": 125,
            "speed": 45,
            "special": 55
        }),
        moves=('whirlwind', 'stomp', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=1004,
        name="Chi-yu",
        types=('Dark', 'Fire'),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 80,
            "defense": 80,
            "speed": 100,
            "special": 135
        }),
        moves=('take down', 'ember', 'flamethrower', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=1005,
        name="Roaring-moon",
        types=('Dragon', 'Dark'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 139,
            "defense": 71,
            "speed": 119,
            "special": 55
        }),
        moves=('fly', 'headbutt', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=1006,
        name="Iron-valiant",
        types=('Fairy', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 74,
            "attack": 130,
            "defense": 90,
            "speed": 116,
            "special": 120
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'swords dance')
    ),
    PokemonBase(
        pokedex_number=1007,
        name="Koraidon",
        types=('Fighting', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 135,
            "defense": 115,
            "speed": 135,
            "special": 85
        }),
        moves=('swords dance', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=1008,
        name="Miraidon",
        types=('Electric', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 100,
            "attack": 85,
            "defense": 100,
            "speed": 135,
            "special": 135
        }),
        moves=('swords dance', 'body slam', 'take down', 'hyper beam')
    ),
    PokemonBase(
        pokedex_number=1009,
        name="Walking-wake",
        types=('Water', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 99,
            "attack": 83,
            "defense": 91,
            "speed": 109,
            "special": 125
        }),
        moves=('body slam', 'take down', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=1010,
        name="Iron-leaves",
        types=('Grass', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 130,
            "defense": 88,
            "speed": 104,
            "special": 70
        }),
        moves=('swords dance', 'take down', 'double edge', 'leer')
    ),
    PokemonBase(
        pokedex_number=1011,
        name="Dipplin",
        types=('Grass', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 80,
            "defense": 110,
            "speed": 40,
            "special": 95
        }),
        moves=('body slam', 'take down', 'hyper beam', 'growth')
    ),
    PokemonBase(
        pokedex_number=1012,
        name="Poltchageist",
        types=('Grass', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 45,
            "speed": 50,
            "special": 74
        }),
        moves=('absorb', 'mega drain', 'solar beam', 'stun spore')
    ),
    PokemonBase(
        pokedex_number=1013,
        name="Sinistcha",
        types=('Grass', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 71,
            "attack": 60,
            "defense": 106,
            "speed": 70,
            "special": 121
        }),
        moves=('hyper beam', 'absorb', 'mega drain', 'solar beam')
    ),
    PokemonBase(
        pokedex_number=1014,
        name="Okidogi",
        types=('Poison', 'Fighting'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 128,
            "defense": 115,
            "speed": 80,
            "special": 58
        }),
        moves=('fire punch', 'ice punch', 'thunder punch', 'body slam')
    ),
    PokemonBase(
        pokedex_number=1015,
        name="Munkidori",
        types=('Poison', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 75,
            "defense": 66,
            "speed": 106,
            "special": 130
        }),
        moves=('scratch', 'psybeam', 'hyper beam', 'toxic')
    ),
    PokemonBase(
        pokedex_number=1016,
        name="Fezandipiti",
        types=('Poison', 'Fairy'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 91,
            "defense": 82,
            "speed": 99,
            "special": 70
        }),
        moves=('swords dance', 'wing attack', 'fly', 'double kick')
    ),
    PokemonBase(
        pokedex_number=1017,
        name="Ogerpon",
        types=('Grass',),
        base_stats=MappingProxyType({
            "hp": 80,
            "attack": 120,
            "defense": 84,
            "speed": 110,
            "special": 60
        }),
        moves=('swords dance', 'slam', 'vine whip', 'double kick')
    ),
    PokemonBase(
        pokedex_number=1018,
        name="Archaludon",
        types=('Steel', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 105,
            "defense": 130,
            "speed": 85,
            "special": 125
        }),
        moves=('swords dance', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=1019,
        name="Hydrapple",
        types=('Grass', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 106,
            "attack": 80,
            "defense": 110,
            "speed": 44,
            "special": 120
        }),
        moves=('body slam', 'take down', 'double edge', 'hydro pump')
    ),
    PokemonBase(
        pokedex_number=1020,
        name="Gouging-fire",
        types=('Fire', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 105,
            "attack": 115,
            "defense": 121,
            "speed": 91,
            "special": 65
        }),
        moves=('stomp', 'double kick', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=1021,
        name="Raging-bolt",
        types=('Electric', 'Dragon'),
        base_stats=MappingProxyType({
            "hp": 125,
            "attack": 73,
            "defense": 91,
            "speed": 75,
            "special": 137
        }),
        moves=('stomp', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=1022,
        name="Iron-boulder",
        types=('Rock', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 120,
            "defense": 80,
            "speed": 124,
            "special": 68
        }),
        moves=('swords dance', 'horn attack', 'body slam', 'take down')
    ),
    PokemonBase(
        pokedex_number=1023,
        name="Iron-crown",
        types=('Steel', 'Psychic'),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 72,
            "defense": 100,
            "speed": 98,
            "special": 122
        }),
        moves=('swords dance', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=1024,
        name="Terapagos",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 90,
            "attack": 65,
            "defense": 85,
            "speed": 60,
            "special": 65
        }),
        moves=('headbutt', 'body slam', 'take down', 'double edge')
    ),
    PokemonBase(
        pokedex_number=1025,
        name="Pecharunt",
        types=('Poison', 'Ghost'),
        base_stats=MappingProxyType({
            "hp": 88,
            "attack": 88,
            "defense": 160,
            "speed": 88,
            "special": 88
        }),
        moves=('toxic', 'night shade', 'recover', 'withdraw')
    ),
]


