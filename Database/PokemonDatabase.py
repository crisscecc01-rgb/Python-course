from types import MappingProxyType
from PkClasses import PokemonBase
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
        moves=('razor wind', 'cut', 'bind', 'vine whip')
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
        moves=('cut', 'bind', 'vine whip', 'headbutt')
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
        moves=('cut', 'bind', 'vine whip', 'headbutt')
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
        moves=('tackle', 'snore', 'bug bite', 'electroweb')
    ),
    PokemonBase(
        pokedex_number=11,
        name="Butterfree",
        types=('Bug', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 60,
            "attack": 45,
            "defense": 50,
            "speed": 70,
            "special": 90
        }),
        moves=('razor wind', 'gust', 'headbutt', 'tackle')
    ),
    PokemonBase(
        pokedex_number=12,
        name="Beedrill",
        types=('Bug', 'Poison'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 40,
            "speed": 75,
            "special": 45
        }),
        moves=('cut', 'headbutt', 'fury attack', 'take down')
    ),
    PokemonBase(
        pokedex_number=13,
        name="Pidgey",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 45,
            "defense": 40,
            "speed": 56,
            "special": 35
        }),
        moves=('razor wind', 'gust', 'wing attack', 'fly')
    ),
    PokemonBase(
        pokedex_number=14,
        name="Pidgeotto",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 63,
            "attack": 60,
            "defense": 55,
            "speed": 71,
            "special": 50
        }),
        moves=('razor wind', 'gust', 'wing attack', 'fly')
    ),
    PokemonBase(
        pokedex_number=15,
        name="Pidgeot",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 83,
            "attack": 80,
            "defense": 75,
            "speed": 101,
            "special": 70
        }),
        moves=('razor wind', 'gust', 'wing attack', 'fly')
    ),
    PokemonBase(
        pokedex_number=16,
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
        pokedex_number=17,
        name="Raticate",
        types=('Normal',),
        base_stats=MappingProxyType({
            "hp": 55,
            "attack": 81,
            "defense": 60,
            "speed": 97,
            "special": 50
        }),
        moves=('cut', 'headbutt', 'tackle', 'body slam')
    ),
    PokemonBase(
        pokedex_number=18,
        name="Spearow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 40,
            "attack": 60,
            "defense": 30,
            "speed": 70,
            "special": 31
        }),
        moves=('razor wind', 'wing attack', 'fly', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=19,
        name="Fearow",
        types=('Normal', 'Flying'),
        base_stats=MappingProxyType({
            "hp": 65,
            "attack": 90,
            "defense": 65,
            "speed": 100,
            "special": 61
        }),
        moves=('razor wind', 'wing attack', 'fly', 'headbutt')
    ),
    PokemonBase(
        pokedex_number=20,
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
]
