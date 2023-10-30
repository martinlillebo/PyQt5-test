'''Dette er hovedfila til editoren'''
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction, QSplitter

# Skiller ut split screen til separat klasse
class CustomSplitter(QSplitter):
    '''En klasse for å instansiere individuelle tekstvinduer'''
    def __init__(self):
        super().__init__()
        self.active_widget = None

    def set_active_widget(self, widget):
        '''Trenger denne for å sette fokus på rett widget'''
        self.active_widget = widget



# Setter opp en editor-klasse
class TextEditor(QMainWindow):
    '''Selve teksteditoren'''
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''Konstruktormetoden'''

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #                   TEXT EDIT AREAS                                 #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Create a QTextEdit for the text editing area
        self.split = CustomSplitter()

        self.text_edit_1 = QTextEdit()
        self.text_edit_2 = QTextEdit()



        self.setCentralWidget(self.split)

        self.split.addWidget(self.text_edit_1)
        self.split.addWidget(self.text_edit_2)

        self.split.set_active_widget(self.text_edit_1)

        self.text_edit_1.focus_event = lambda event: self.split.set_active_widget(self.text_edit_1)
        self.text_edit_2.focus_event = lambda event: self.split.set_active_widget(self.text_edit_2)

        # Endrer tekstområdet til mørkere design
        stylesheet_text_area = "background-color: #333; color: white; border: 2px solid #555;"

        self.text_edit_1.setStyleSheet(stylesheet_text_area)
        self.text_edit_2.setStyleSheet(stylesheet_text_area)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #                   TOOLBAR                                         #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Lager en toolbar
        toolbar = QToolBar("Toolbar?")
        self.addToolBar(toolbar)

        # Lager open og save knapper til "fil
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)

        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)

        # Lager "fil"-knapp til toolbar
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #                   *******                                         #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Create a central widget to hold the layout
        self.setCentralWidget(self.split)

        # Initialize the application window
        self.setWindowTitle('Hobbyprosjekt 🙂')
        self.setGeometry(100, 100, 800, 600)

    def open_file(self):
        '''For å åpne tekstfiler'''
        # Implement the open file function
        file_path = QFileDialog.getOpenFileName(self, 'Open File', '',
            'Text Files (*.txt);;All Files (*)')
        if file_path:
            # Read the file and display its content in the QTextEdit
            with open(file_path, 'r', encoding="utf-8") as file:
                self.text_edit_1.setPlainText(file.read())

    def save_file(self):
        '''For å lagre tekstfiler'''
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File',
            '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(self.text_edit_1.toPlainText())

    def focus_event(self):
        '''Tror ikke denne gjør noe nyttig lengre'''
        print("Gained focus!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setCursorFlashTime(500)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
