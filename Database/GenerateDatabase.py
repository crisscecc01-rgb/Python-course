import requests

# --- CONFIGURAZIONE ---
NUMERO_POKEMON_DESIDERATI = 20
FILE_POKEMON = "PokemonDatabase.py"
FILE_MOSSE = "MovesDatabase.py"


def analizza_effetto(dati_mossa):
    cambiamenti_stat = dati_mossa.get("stat_changes", [])
    if not cambiamenti_stat:
        return "None"

    bersaglio_api = dati_mossa.get("target", {}).get("name", "")
    if "user" in bersaglio_api:
        bersaglio = "self"
    else:
        bersaglio = "opponent"

    target_stat = [f'"{bersaglio}"']
    changes = []

    for cambio in cambiamenti_stat:
        stat_nome = cambio["stat"]["name"].replace("-", "_")
        valore_cambio = cambio["change"]
        target_stat.append(f'"{stat_nome}"')

        # Gestione del segno + per valori positivi
        segno = "+" if valore_cambio > 0 else ""
        changes.append(f"{segno}{valore_cambio}")

    target_stat_str = ", ".join(target_stat)
    changes_str = ", ".join(changes)

    return f'{{"target_stat": [{target_stat_str}], "change": [{changes_str}]}}'


def genera_database():
    pokemon_selezionati = []
    mosse_approvate = {}  # Dizionario: nome_mossa -> dati_mossa
    cache_mosse_api = {}  # Cache per non riscaricare la stessa mossa decine di volte

    id_pkmn = 1
    print(f"Inizio ricerca di {NUMERO_POKEMON_DESIDERATI} Pokémon con mosse di solo attacco...")

    while len(pokemon_selezionati) < NUMERO_POKEMON_DESIDERATI and id_pkmn <= 151:
        url_pkmn = f"https://pokeapi.co/api/v2/pokemon/{id_pkmn}"
        resp_pkmn = requests.get(url_pkmn)

        if resp_pkmn.status_code == 200:
            dati_pkmn = resp_pkmn.json()
            mosse_pkmn_valide = []

            # Analizziamo le mosse che questo Pokémon può imparare
            for mossa_info in dati_pkmn["moves"]:
                nome_mossa = mossa_info["move"]["name"].replace("-", " ")
                url_mossa = mossa_info["move"]["url"]

                # Scarichiamo i dati della mossa solo se non l'abbiamo già fatto
                if url_mossa not in cache_mosse_api:
                    resp_mossa = requests.get(url_mossa)
                    if resp_mossa.status_code == 200:
                        dati_mossa = resp_mossa.json()

                        # IL TUO FILTRO: Accuracy e Power NON devono essere None
                        if dati_mossa.get("power") is not None and dati_mossa.get("accuracy") is not None:
                            cache_mosse_api[url_mossa] = dati_mossa
                        else:
                            cache_mosse_api[url_mossa] = None  # Mossa scartata
                    else:
                        cache_mosse_api[url_mossa] = None

                # Se la mossa ha superato i controlli, la assegniamo al Pokémon
                dati_mossa_valida = cache_mosse_api.get(url_mossa)
                if dati_mossa_valida:
                    mosse_pkmn_valide.append(nome_mossa)
                    mosse_approvate[nome_mossa] = dati_mossa_valida  # La mettiamo in coda per il file delle mosse

                # Appena ne troviamo 4 valide, smettiamo di cercare mosse per questo Pokémon
                if len(mosse_pkmn_valide) == 4:
                    break

            # Se il Pokémon ha effettivamente 4 mosse valide, lo aggiungiamo al nostro database!
            if len(mosse_pkmn_valide) == 4:
                nome = dati_pkmn["name"].capitalize()
                tipi = tuple(t["type"]["name"].capitalize() for t in dati_pkmn["types"])
                stats = {s["stat"]["name"]: s["base_stat"] for s in dati_pkmn["stats"]}

                pokemon_selezionati.append({
                    "nome": nome,
                    "tipi": tipi,
                    "stats": stats,
                    "mosse": tuple(mosse_pkmn_valide)
                })
                print(f"[{len(pokemon_selezionati)}/{NUMERO_POKEMON_DESIDERATI}] Trovato {nome} con 4 mosse valide!")

        id_pkmn += 1

    # --- FASE 2: SCRITTURA DEL FILE POKEMON DATABASE ---
    print(f"\nScrittura di {FILE_POKEMON}...")
    with open(FILE_POKEMON, "w", encoding="utf-8") as f:
        f.write("from types import MappingProxyType\n")
        f.write("from PkClasses import PokemonBase\n")
        f.write("PokemonList = [\n")

        for idx, pk in enumerate(pokemon_selezionati):
            f.write(
                f"    PokemonBase(\n"
                f"        pokedex_number={idx + 1},\n"
                f"        name=\"{pk['nome']}\",\n"
                f"        types={pk['tipi']},\n"
                f"        base_stats=MappingProxyType({{\n"
                f"            \"hp\": {pk['stats'].get('hp', 0)},\n"
                f"            \"attack\": {pk['stats'].get('attack', 0)},\n"
                f"            \"defense\": {pk['stats'].get('defense', 0)},\n"
                f"            \"speed\": {pk['stats'].get('speed', 0)},\n"
                f"            \"special\": {pk['stats'].get('special-attack', 0)}\n"
                f"        }}),\n"
                f"        moves={pk['mosse']}\n"
                f"    ),\n"
            )
        f.write("]\n")

    # --- FASE 3: SCRITTURA DEL FILE MOVES DATABASE ---
    print(f"Scrittura di {FILE_MOSSE}...")
    with open(FILE_MOSSE, "w", encoding="utf-8") as f:
        f.write("from Move import Move\n")
        f.write("MovesList = {\n")

        for nome_mossa, dati_mossa in mosse_approvate.items():
            tipo = dati_mossa["type"]["name"]
            categoria = dati_mossa.get("damage_class", {}).get("name", "physical")
            potenza = dati_mossa.get("power")
            precisione = dati_mossa.get("accuracy") / 100.0  # Convertito in decimale (es. 100 -> 1.0)
            pp = dati_mossa.get("pp")
            effetto_str = analizza_effetto(dati_mossa)

            f.write(
                f'    "{nome_mossa}": Move('
                f'"{nome_mossa}", "{tipo}", "{categoria}", {potenza}, {precisione}, {pp}, {effetto_str}'
                f'),\n'
            )

        f.write("}\n")

    print("\nFinito! I database sono perfettamente allineati e pronti all'uso.")


if __name__ == "__main__":
    genera_database()