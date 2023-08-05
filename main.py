import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QStyle
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
import string
import functions as f

p,d,c,a =f.leggi_file_e_struttura("lista.txt")

# Function to set the rounded style for buttons
def set_rounded_button_style(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #3daee9;
            color: #ffffff;
            padding: 10px;
            border-radius: 15px;  /* Adjust the value to change the roundness */
        }
        QPushButton:hover {
            background-color: #3dbbe9;
        }
    """)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fanta_Shalom_24")

        # Shuffle and initialize arrays
        portieri = f.shuffle_array(p)
        difensori = f.shuffle_array(d)
        centrocampisti = f.shuffle_array(c)
        attaccanti = f.shuffle_array(a)

        # Set the first element to "LOADING...." for each array after shuffling
        Seleziona_Ruolo = []
        portieri = ["LOADING...."] + portieri[1:]
        difensori = ["LOADING...."] + difensori[1:]
        centrocampisti = ["LOADING...."] + centrocampisti[1:]
        attaccanti = ["LOADING...."] + attaccanti[1:]

        # Store the arrays in a dictionary
        self.arrays = {
            "Seleziona Ruolo": Seleziona_Ruolo,
            "PORTIERI": portieri,
            "DIFFENSORI": difensori,
            "CENTROCAMPISTI": centrocampisti,
            "ATTACCANTI": attaccanti,
        }

        # Variable to keep track of the current index of the array
        self.current_index = 0

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Load the icon image
        icon = QIcon("Flag.png")

        # Set the window icon
        self.setWindowIcon(icon)

        self.label = QLabel("SHALOM!")
        self.label.setFont(QFont("Helvetica", 50, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.array_combobox = QComboBox()
        self.array_combobox.addItems(list(self.arrays.keys()))
        self.array_combobox.setCurrentText("Seleziona ruolo")
        self.array_combobox.currentTextChanged.connect(self.change_array)

        # Set rounded style for the combobox
        self.array_combobox.setStyleSheet("""
            QComboBox {
                background-color: #3daee9;
                color: #ffffff;
                border: 2px solid #3daee9;
                border-radius: 15px;  /* Adjust the value to change the roundness */
                padding: 5px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow_white.png);  /* Set your custom down arrow image here */
            }
        """)

        layout.addWidget(self.array_combobox)

        # Use QHBoxLayout for the buttons
        button_layout = QHBoxLayout()
        self.previous_button = QPushButton("Giocatore precedente", clicked=self.show_previous_player)
        self.next_button = QPushButton("Giocatore successivo", clicked=self.show_next_player)

        # Set rounded button styles
        set_rounded_button_style(self.previous_button)
        set_rounded_button_style(self.next_button)

        # Hide the buttons initially
        self.hide_buttons()

        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Set the application style sheet for dark mode
        dark_mode_stylesheet = """
            QWidget {
                background-color: #282c34;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
        """

        self.setStyleSheet(dark_mode_stylesheet)

    def show_next_player(self):
        if self.current_index < len(self.content_array):
            player_name = self.content_array[self.current_index]
            self.label.setText(player_name)

            if self.current_index == len(self.content_array) // 2:
                self.label.setFont(QFont("Helvetica", 50, QFont.Bold))
            else:
                self.label.setFont(QFont("Helvetica", 50, QFont.Bold))

            self.current_index += 1

    def show_previous_player(self):
        if self.current_index > 0:
            self.current_index -= 1
            player_name = self.content_array[self.current_index]
            self.label.setText(player_name)

    def show_buttons(self):
        # Show the buttons after selecting an array
        self.previous_button.show()
        self.next_button.show()

    def hide_buttons(self):
        # Hide the buttons when selecting a new array
        self.previous_button.hide()
        self.next_button.hide()

    def change_array(self):
        selected_array = self.array_combobox.currentText()
        self.content_array = self.arrays[selected_array]
        self.current_index = 0
        self.show_next_player()

        # Call the function to show the buttons
        self.show_buttons()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Set the application style to "Fusion"
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
