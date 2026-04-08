from encodings import normalize_encoding
"""Prendono i dati grezzi e li trasformano in Oggetti Python"""

class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd

    def __str__(self):
        """Definisce come l'oggetto viene stampato"""
        return f'{self.nome} ({self.codins})'

    def __eq__(self, other):
        """Per confrontare due corsi capendo se sono uguali"""
        return self.codins == other.codins

    def __hash__(self):
        """Per inserirli in un set o come chiave di un dizionario"""
        return hash(self.codins)