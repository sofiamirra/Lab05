from database.DB_connect import get_connection
from model.corso import Corso # importiamo gli oggetti Corso

class CorsoDAO:

    @staticmethod
    def get_tutti_corsi():
        """Funzione per popolare il menù a tendina con tutti i corsi"""

        # Apertura connessione
        cnx = get_connection()
        if cnx is None:
            print("Errore connessione")
            return []

        # Creazione cursore con struttura dizionario
        cursor = cnx.cursor(dictionary=True)

        # Esecuzione della query
        query = "SELECT * FROM corso"
        cursor.execute(query)

        # Gestione risultati
        result = []
        for row in cursor:
            result.append(Corso(**row))

        # Chiusura connessione
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_corsi_studente(matricola):
        """Funzione per ottenere i corsi a cui è iscritto una matricola (Key: matricola)"""

        # Apertura connessione
        cnx = get_connection()
        if cnx is None:
            print("Errore connessione")
            return []

        # Creazione cursore con struttura dizionario
        cursor = cnx.cursor(dictionary=True)

        # Esecuzione della query: tutti i dati del corso dove la matricola combacia
        query = """SELECT c.* FROM corso c, iscrizione i
                 WHERE c.codins = i.codins AND i.matricola = %s"""
        cursor.execute(query, (matricola,))

        # Gestione risultati
        result = []
        for row in cursor:
            result.append(Corso(**row))

        # Chiusura connessione
        cursor.close()
        cnx.close()

        return result