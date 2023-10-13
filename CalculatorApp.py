# calculator.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()
        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        # Create a stylesheet for the buttons
        button_style = "QPushButton { background-color: #333; color: white; font-size: 16px; border: 2px solid #666; }"
        
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]

        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            # Apply the stylesheet to the buttons
            button.setStyleSheet(button_style)
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        if button.text() == "=":
            try:
                result = str(eval(self.text_edit.text()))
                self.text_edit.setText(result)
            except Exception:
                self.text_edit.setText("Error")
        elif button.text() == "C":
            self.text_edit.clear()
        else:
            current_text = self.text_edit.text()
            new_text = current_text + button.text()
            self.text_edit.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec_())
