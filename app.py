from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize expression and display text
        self.expression = ""
        self.setWindowTitle("iPhone Calculator Clone")
        self.setGeometry(100, 100, 330, 500)
        self.setStyleSheet("background-color: black;")

        # Display layout
        self.display_label = QLabel("0", self)
        self.display_label.setAlignment(Qt.AlignRight)
        self.display_label.setFont(QFont("Arial", 30))
        self.display_label.setStyleSheet("color: white; background-color: black; padding: 10px;")
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display_label)
        
        # Button layout
        buttons = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # Create buttons
        self.ac_button = None  # Initialize a reference for the AC/C button
        for row in buttons:
            row_layout = QHBoxLayout()
            for label in row:
                if label == "0":
                    button = self.create_button(label, "gray", colspan=2)
                    row_layout.addWidget(button, 2)  # Span two columns
                else:
                    # Set color based on label
                    if label == "AC":
                        button = self.create_button(label, "lightgray")
                        self.ac_button = button  # Store the AC button reference
                    elif label in ["+/-", "%"]:
                        bg_color = "lightgray"
                        button = self.create_button(label, bg_color)
                    elif label in ["÷", "×", "-", "+", "="]:
                        bg_color = "orange"
                        button = self.create_button(label, bg_color)
                    else:
                        bg_color = "gray"
                        button = self.create_button(label, bg_color)
                    row_layout.addWidget(button)
            main_layout.addLayout(row_layout)

        self.setLayout(main_layout)

    def create_button(self, text, color, colspan=1):
        button = QPushButton(text, self)
        button.setFont(QFont("Arial", 20))
        
        # Define styles based on button color
        if color == "lightgray":
            button.setStyleSheet(f"""
                QPushButton {{
                    color: black;
                    background-color: lightgray;
                    border-radius: 35px;
                    min-width: 70px;
                    min-height: 70px;
                }}
                QPushButton:pressed {{
                    background-color: #e0e0e0; /* Slightly lighter shade */
                }}
            """)
        elif color == "gray":
            button.setStyleSheet(f"""
                QPushButton {{
                    color: white;
                    background-color: gray;
                    border-radius: 35px;
                    min-width: 70px;
                    min-height: 70px;
                }}
                QPushButton:pressed {{
                    background-color: #a9a9a9; /* Lighter shade */
                }}
            """)
        elif color == "orange":
            button.setStyleSheet(f"""
                QPushButton {{
                    color: white;
                    background-color: orange;
                    border-radius: 35px;
                    min-width: 70px;
                    min-height: 70px;
                }}
                QPushButton:pressed {{
                    color: orange;
                    background-color: white; /* Inverted color */
                }}
            """)
        
        button.clicked.connect(lambda: self.on_button_click(text))
        return button

    def on_button_click(self, char):
        if char == "AC" or char == "C":
            # Reset the expression and display label
            self.expression = ""
            self.display_label.setText("0")
            # Reset the AC button text back to "AC" after clearing
            self.ac_button.setText("AC")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display_label.setText(result)
                self.expression = result
            except:
                self.display_label.setText("Error")
                self.expression = ""
        elif char == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display_label.setText(self.expression)
        elif char in ["+", "-", "×", "÷"]:
            char = "*" if char == "×" else "/" if char == "÷" else char
            self.expression += char
            self.display_label.setText(self.expression)
        else:
            # Append the character to the expression
            self.expression += char
            self.display_label.setText(self.expression)
            # Change AC to C as there's now an expression
            if self.ac_button.text() == "AC":
                self.ac_button.setText("C")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
