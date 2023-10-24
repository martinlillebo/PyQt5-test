import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QFileDialog, QToolBar, QAction
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
        # Create a QTextEdit for the text editing area
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Endrer tekstområdet til mørkere design
        self.text_edit.setStyleSheet("background-color: #333; color: white; border: 2px solid #555;")

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

        # Create a layout for the buttons
        button_layout = QVBoxLayout()

        # Set up the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

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


# app = QApplication(sys.argv)  # Create a PyQt5 application

# window = TextEditor()  # Create the main application window
# window.setWindowTitle('Widgets and Layouts')

# central_widget = QWidget()  # Create a central widget
# window.setCentralWidget(central_widget)  # Set it as the central widget

# # Create widgets
# label = QLabel('Hello, PyQt5!')
# button = QPushButton('Click Me')
# button.clicked.connect(lambda: label.setText('Button Clicked'))
# button2 = QPushButton("test2")
# lineTest = QLineEdit()

# # Create a layout and add widgets to it
# layout = QHBoxLayout(central_widget)  # Use central_widget as the parent
# layout.addWidget(label)
# layout.addWidget(button)
# layout.addWidget(button2)
# layout.addWidget(lineTest)

# layout.setAlignment(Qt.AlignLeft)

# Keypressevent som lukker vinduet om ESC trykkes




# Kobler event-et til hovedvinduet
# window.keyPressEvent = escapeEvent

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())


# window.show()  # Display the main window
#sys.exit(app.exec_())  # Start the application event loop

