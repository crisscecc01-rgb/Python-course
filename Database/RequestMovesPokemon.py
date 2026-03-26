import requests

# --- CONFIGURAZIONE ---
# Numero di mosse da scaricare (La prima generazione ha 165 mosse, in totale ad oggi sono circa 900)
NUMERO_MOSSE = 1000
NOME_FILE_OUTPUT = "MovesDatabase.py"


def ottieni_dati_mossa(id_mossa):
    url = f"https://pokeapi.co/api/v2/move/{id_mossa}"
    risposta = requests.get(url)
    if risposta.status_code != 200:
        return None
    return risposta.json()


def analizza_effetto(dati_mossa):
    # Estraiamo i cambiamenti alle statistiche
    cambiamenti_stat = dati_mossa.get("stat_changes", [])
    if not cambiamenti_stat:
        return "None"

    # Capire chi è il bersaglio
    bersaglio_api = dati_mossa.get("target", {}).get("name", "")
    if "user" in bersaglio_api:
        bersaglio = "self"
    else:
        bersaglio = "opponent"

    target_stat = [f'"{bersaglio}"']
    changes = []

    # Raccogliamo tutte le statistiche modificate e i loro valori
    for cambio in cambiamenti_stat:
        # Sostituiamo i trattini con underscore per le statistiche (es. special-attack -> special_attack)
        stat_nome = cambio["stat"]["name"].replace("-", "_")
        valore_cambio = cambio["change"]

        target_stat.append(f'"{stat_nome}"')

        # Aggiungiamo il segno '+' per i valori positivi, come nel tuo esempio
        segno = "+" if valore_cambio > 0 else ""
        changes.append(f"{segno}{valore_cambio}")

    # Costruiamo la stringa del dizionario
    target_stat_str = ", ".join(target_stat)
    changes_str = ", ".join(changes)

    return f'{{"target_stat": [{target_stat_str}], "change": [{changes_str}]}}'


def genera_file_database_mosse():
    print(f"Inizio il download di {NUMERO_MOSSE} mosse. Attendere...")

    with open(NOME_FILE_OUTPUT, "w", encoding="utf-8") as f:
        # Intestazione del file
        f.write("# Incolla qui sopra la definizione della tua classe Move\n\n")
        f.write("MovesList = {\n")

        for i in range(1, NUMERO_MOSSE + 1):
            dati = ottieni_dati_mossa(i)
            if not dati:
                print(f"Errore nel recupero della mossa #{i}")
                continue

            # Parsing dei campi principali
            nome = dati["name"].replace("-", " ")
            tipo = dati["type"]["name"]

            # La categoria può essere physical, special o status
            categoria = dati.get("damage_class", {}).get("name", "status")

            potenza = dati.get("power")
            potenza_str = str(potenza) if potenza is not None else "None"

            # La precisione viene passata come percentuale intera (es 95), la portiamo a float (0.95)
            precisione = dati.get("accuracy")
            precisione_str = str(precisione / 100.0) if precisione is not None else "None"

            pp = dati.get("pp")
            pp_str = str(pp) if pp is not None else "None"

            # Generazione del blocco effect
            effetto_str = analizza_effetto(dati)

            # Formattazione della riga
            riga_mossa = (
                f'    "{nome}": Move('
                f'"{nome}", "{tipo}", "{categoria}", {potenza_str}, {precisione_str}, {pp_str}, {effetto_str}'
                f'),\n'
            )

            f.write(riga_mossa)
            print(f"Salvata: {nome} (#{i})")

        # Chiusura del dizionario
        f.write("}\n")

    print(f"\nFinito! Le tue mosse sono salvate nel file '{NOME_FILE_OUTPUT}'.")


if __name__ == "__main__":
    genera_file_database_mosse()