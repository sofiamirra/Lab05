class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.CDS = CDS

    def __str__(self):
        return f'{self.nome}, {self.cognome} ({self.matricola})'

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)