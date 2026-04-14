import flet as ft


class View:
    def __init__(self, page: ft.Page):
        # super().__init__()
        # Inizializzazione elementi fisici interfaccia
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        self._title = None
        # elementi riga 1
        self.dd_corso = None # menù a tendina
        self.btn_cerca_iscritti = None # bottone
        # elementi riga 2
        self.txt_matricola = None # contenuto testuale
        self.txt_nome = None
        self.txt_cognome = None
        # elementi riga 3
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        # ListView per stampare risposte
        self.txt_result = None

    def load_interface(self):
        """Funzione che carica gli elementi grafici sulla pagina"""
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # Costruzione riga 1
        self.dd_corso = ft.Dropdown(
            label="corso",
            width=200,
            hint_text="Selezionare un corso",
            options = [] # i corsi li prenderemo dal database
        )

        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_cerca_iscritti)
        row1 = ft.Row([self.dd_corso, self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Costruzione riga 2
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
        )

        self.txt_nome = ft.TextField(
            label="nome",
            width=200,
            read_only=True, # campo non editabile
        )

        self.txt_cognome = ft.TextField(
            label="cognome",
            width=200,
            read_only=True, # campo non editabile
        )
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Costruzione riga 3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente",
                                                    on_click=self._controller.handle_cerca_studente)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi",
                                                    on_click=self._controller.handle_cerca_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi",
                                                 on_click=self._controller.handle_iscrivi)
        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Aggiungiamo tutto alla pagina
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

       # List View stampa risultati
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
