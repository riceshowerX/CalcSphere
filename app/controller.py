from app.model import CalculatorModel
from app.utils import HistoryManager
from PyQt6.QtWidgets import QListWidgetItem

class CalculatorController:
    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel()
        self.history = HistoryManager()
        self.connect_signals()

    def connect_signals(self):
        # 按钮点击事件
        for btn in self.view.findChildren(QPushButton):
            btn.clicked.connect(lambda _, b=btn: self.handle_input(b.text()))
        
        # 主题切换
        self.view.theme_menu.currentTextChanged.connect(self.change_theme)
        
        # 历史记录显示
        self.view.history_list.itemClicked.connect(self.load_history_item)

    def handle_input(self, text):
        current = self.view.display.text()
        
        if text == "=":
            result = self.model.calculate(current)
            self.view.display.setText(result)
            self.history.add(f"{current} = {result}")
        elif text == "C":
            self.view.display.clear()
        else:
            self.view.display.setText(current + text)

    def change_theme(self, theme_name):
        with open(f"assets/styles/{theme_name.lower().replace(' ', '_')}.qss", "r") as f:
            self.view.setStyleSheet(f.read())

    def load_history_item(self, item):
        expression = item.text().split(" = ")[0]
        self.view.display.setText(expression)