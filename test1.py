import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QFileDialog, QToolBar, QAction, QSplitter
from PyQt5.QtWidgets import QHBoxLayout # QH = QHorizontal, QV = QVertical
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

# Setter opp en editor-klasse
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Alt i initUI kjøres automatisk siden den kalles i konstruktoren ovenfor
    def initUI(self):

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #                   TEXT EDIT AREAS                                 #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # Create a QTextEdit for the text editing area
        splitter = QSplitter(self)
        self.text_edit_1 = QTextEdit()
        self.text_edit_2 = QTextEdit()
        self.setCentralWidget(self.text_edit_1)

        splitter.addWidget(self.text_edit_1)
        splitter.addWidget(self.text_edit_2)        

        # Endrer tekstområdet til mørkere design
        self.text_edit_1.setStyleSheet("background-color: #333; color: white; border: 2px solid #555;")
        self.text_edit_2.setStyleSheet("background-color: #333; color: white; border: 2px solid #555;")

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

        # Set up the main layout
        main_layout = QVBoxLayout() # <-------- QVBOX = Vertikal orientering på widgetene
        main_layout.addWidget(self.text_edit_1)

        # Create a central widget to hold the layout
#       central_widget = QWidget()
        splitter.setLayout(main_layout)
        self.setCentralWidget(splitter)

        # Initialize the application window
        self.setWindowTitle('Hobbyprosjekt 🙂')
        self.setGeometry(100, 100, 800, 600)

        self.keyPressEvent = self.close_with_esc
    
    def close_with_esc(self, event):
        if event.key() == Qt.Key_Escape:
            app.quit()

    def open_file(self):
        # Implement the open file function
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            # Read the file and display its content in the QTextEdit
            with open(file_path, 'r') as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        # Implement the save file function
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            # Write the text from the QTextEdit to the selected file
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
