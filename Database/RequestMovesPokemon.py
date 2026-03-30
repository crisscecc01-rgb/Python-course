import requests

# --- CONFIGURAZIONE ---
# Numero di mosse da scaricare (La prima generazione ha 165 mosse)
NUMERO_MOSSE = 165
NOME_FILE_OUTPUT = "MovesDatabase.py"

# --- DEFINIZIONE DELLA CLASSE DA SCRIVERE NEL FILE ---


def ottieni_dati_mossa(id_mossa):
    url = f"https://pokeapi.co/api/v2/move/{id_mossa}"
    risposta = requests.get(url)
    if risposta.status_code != 200:
        return None
    return risposta.json()


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


def genera_file_database_mosse():
    print(f"Inizio il download di {NUMERO_MOSSE} mosse. Attendere...")

    with open(NOME_FILE_OUTPUT, "w", encoding="utf-8") as f:
        # 1. Scriviamo la classe Move in cima al file
        f.write("from PkClasses import Move\n")
        # 2. Apriamo il dizionario delle mosse
        f.write("MovesList = {\n")

        for i in range(1, NUMERO_MOSSE + 1):
            dati = ottieni_dati_mossa(i)
            if not dati:
                print(f"Errore nel recupero della mossa #{i}")
                continue

            nome = dati["name"].replace("-", " ")
            tipo = dati["type"]["name"]
            categoria = dati.get("damage_class", {}).get("name", "status")

            potenza = dati.get("power")
            potenza_str = str(potenza) if potenza is not None else "None"

            precisione = dati.get("accuracy")
            precisione_str = str(precisione / 100.0) if precisione is not None else "None"

            pp = dati.get("pp")
            pp_str = str(pp) if pp is not None else "None"

            effetto_str = analizza_effetto(dati)

            # 3. Formattiamo e scriviamo la riga per la singola mossa
            riga_mossa = (
                f'    "{nome}": Move('
                f'"{nome}", "{tipo}", "{categoria}", {potenza_str}, {precisione_str}, {pp_str}, {effetto_str}'
                f'),\n'
            )

            f.write(riga_mossa)
            print(f"Salvata: {nome} (#{i})")

        # 4. Chiudiamo il dizionario
        f.write("}\n")

    print(f"\nFinito! Le tue mosse sono salvate nel file '{NOME_FILE_OUTPUT}'.")


if __name__ == "__main__":
    genera_file_database_mosse()