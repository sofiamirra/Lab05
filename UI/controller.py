import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    # Cerca gli studenti iscritti ad un corso
    def handle_cerca_iscritti(self, e):
        cod_corso = self._view.dd_corso.value # selezione dell'utente nel dropdown
        if cod_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        studenti = self.model.get_studenti(cod_corso) # lista di studenti dal Model
        self._view.txt_result.controls.clear() # pulisce l'area di stampa
        if not studenti:
            self._view.txt_result.controls.append(ft.Text(f"Nessun iscritto trovato per questo corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso: "))
            for s in studenti:
                self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()

    def handle_cerca_studente(self, e):
        matricola = self._view.matricola.value  # selezione della matricola nell'input
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        studente = self.model.get_studente_by_matricola(matricola)  # lista di studenti dal Model
        if studente is None:
            self._view.create_alert("Matricola non trovata!")
            return
        # Dalla matricola completa in automatico nome e cognome dello studente
        self._view.txt_nome.value = studente.nome
        self._view.txt_cognome.value = studente.cognome
        self._view.update_page()

    def handle_cerca_corsi(self, e):
        matricola = self._view.matricola.value  # selezione della matricola nell'input
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        studente = self.model.get_studente_by_matricola(matricola)  # verifichiamo che lo studente esista
        if studente is None:
            self._view.create_alert("Matricola non trovata!")
            return

        corsi = self._model.get_corsi_studente(matricola)
        self._view.txt_result.controls.clear()  # pulisce l'area di stampa
        if not corsi:
            self._view.txt_result.controls.append(ft.Text(f"Lo studente non è iscritto ad alcun corso!"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi"))
            for c in corsi:
                self._view.txt_result.controls.append(ft.Text(c))

    def handle_iscriviti(self, e):
        self._view.create_alert("Non ancora implementata")

    def fill_dropdown(self):
        corsi = self._model.get_tutti_corsi()
        for c in corsi:
            self._view.dd_corso.options.append(ft.dropdown.Option(key=c.codins, text=str(c)))
        self._view.update_page()