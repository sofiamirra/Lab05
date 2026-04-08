from database.DB_connect import get_connection
# Importiamo lo stampo dello studente
from model.studente import Studente


class StudenteDAO:

    @staticmethod
    def get_studenti_corso(codins):
        """Recupera tutti gli studenti iscritti a un determinato corso (Punto 2 della traccia)"""

        # Apertura connessione con le parentesi corrette!
        cnx = get_connection()
        if cnx is None:
            print("Errore connessione")
            return [] # lista vuota

        cursor = cnx.cursor(dictionary=True)

        # JOIN tra studente e iscrizione per trovare chi frequenta quel codins
        query = """SELECT s.* FROM studente s, iscrizione i 
                   WHERE s.matricola = i.matricola AND i.codins = %s"""

        cursor.execute(query, (codins,)) # tupla con un solo elemento

        # Creiamo l'oggetto Studente per ogni riga trovata
        result = []
        for row in cursor:
            result.append(Studente(**row))

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def get_studente_by_matricola(matricola):
        """Cerca un singolo studente passandogli la matricola (Punto 3 della traccia)"""

        # Apertura connessione
        cnx = get_connection()
        if cnx is None:
            print("Errore connessione")
            return None  # Qui restituiamo None, non una lista vuota, perché cerchiamo una persona sola

        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM studente WHERE matricola = %s"

        cursor.execute(query, (matricola,))

        # fetchone() ci restituisce il primo dizionario trovato, oppure None se la matricola non esiste
        row = cursor.fetchone()

        cursor.close()
        cnx.close()

        # Se abbiamo trovato una riga, la "impacchettiamo" nell'oggetto Studente
        if row is not None:
            return Studente(**row)
        else:
            return None