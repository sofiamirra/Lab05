"""Il Controller non deve mai parlare con il DAO, ma deve passare per il Model,
che contiene controlli e calcoli logici senza inquinare la grafica"""
from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:
    def __init__(self):
        pass

    def get_tutti_corsi(self):
        # Chiede al DAO l'elenco completo dei corsi
        return CorsoDAO.get_tutti_corsi()

    def get_corsi_studente(self, matricola):
        # Chiede al DAO l'elenco dei corsi di uno studente
        if not matricola.isdigit():
            return [] # lista vuota se la matricola non ha senso
        return CorsoDAO.get_corsi_studente(matricola)

    def get_studenti_corso(self, codins):
        if codins is None or codins == "":
            return []
        # Chiamiamo StudenteDAO invece di CorsoDAO
        return StudenteDAO.get_studenti_corso(codins)

    def get_studente_by_matricola(self, matricola):
        if not matricola.isdigit():
            return []
        return StudenteDAO.get_studente_by_matricola(matricola)