import sys
from PyQt6.QtWidgets import QApplication
from app.view import CalculatorView
from app.controller import CalculatorController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = CalculatorView()
    controller = CalculatorController(view)
    view.show()
    sys.exit(app.exec())