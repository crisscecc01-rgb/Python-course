import requests

# --- configuration ---
NUMERO_POKEMON = 1025
NOME_FILE_OUTPUT = "PokemonDatabase.py"


def ottieni_dati_pokemon(id_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
    risposta = requests.get(url)
    if risposta.status_code != 200:
        return None
    return risposta.json()


def genera_file_database():
    print(f"Inizio il download di {NUMERO_POKEMON} Pokémon.")

    with open(NOME_FILE_OUTPUT, "w", encoding="utf-8") as f:
        # 1. Scriviamo le importazioni e la struttura della classe
        f.write("from types import MappingProxyType\n")
        f.write("from dataclasses import dataclass\n\n")
        f.write("@dataclass\n")
        f.write("class PokemonBase:\n")
        f.write("    pokedex_number: int\n")
        f.write("    name: str\n")
        f.write("    types: tuple\n")
        f.write("    base_stats: MappingProxyType\n")
        f.write("    moves: tuple\n\n")

        # 2. Apriamo la lista
        f.write("PokemonList = [\n")

        # 3. Cicliamo per ogni Pokémon e scriviamo i dati
        for i in range(1, NUMERO_POKEMON + 1):
            dati = ottieni_dati_pokemon(i)
            if not dati:
                print(f"Errore nel recupero del Pokémon #{i}")
                continue

            # Estraiamo il nome e i tipi
            nome = dati["name"].capitalize()
            tipi = tuple(t["type"]["name"].capitalize() for t in dati["types"])

            # Estraiamo le statistiche
            # (Mappiamo l'attacco speciale come 'special' per rispettare la tua struttura)
            stats = {s["stat"]["name"]: s["base_stat"] for s in dati["stats"]}
            hp = stats.get("hp", 0)
            attack = stats.get("attack", 0)
            defense = stats.get("defense", 0)
            speed = stats.get("speed", 0)
            special = stats.get("special-attack", 0)

            # Estraiamo le prime 4 mosse imparabili
            mosse = tuple(m["move"]["name"].replace("-", " ") for m in dati["moves"][:4])

            # Formattiamo il blocco di codice per questo Pokémon
            blocco_pokemon = (
                f"    PokemonBase(\n"
                f"        pokedex_number={i},\n"
                f"        name=\"{nome}\",\n"
                f"        types={tipi},\n"
                f"        base_stats=MappingProxyType({{\n"
                f"            \"hp\": {hp},\n"
                f"            \"attack\": {attack},\n"
                f"            \"defense\": {defense},\n"
                f"            \"speed\": {speed},\n"
                f"            \"special\": {special}\n"
                f"        }}),\n"
                f"        moves={mosse}\n"
                f"    ),\n"
            )

            f.write(blocco_pokemon)
            print(f"Salvato: {nome} (#{i})")

        # 4. Chiudiamo la lista
        f.write("]\n")

    print(f"\nFinito! Il tuo database è pronto nel file '{NOME_FILE_OUTPUT}'.")


if __name__ == "__main__":
    genera_file_database()