from PyQt6.QtWidgets import (  # 确保包含所有需要的组件
    QMainWindow, QLineEdit, QGridLayout, QPushButton, QWidget, 
    QToolBar, QComboBox, QListWidget, QVBoxLayout  # 新增 QVBoxLayout
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
from config.constants import PRIMARY_COLOR, SECONDARY_COLOR
class CalculatorView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.initUI()

    def initUI(self):
        # 主容器
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        # 显示屏
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet(f"font-size: 36px; padding: 10px; background: {PRIMARY_COLOR}; color: white;")
        layout.addWidget(self.display)

        # 按钮布局
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["(", ")", "C", "^"],
            ["sin", "cos", "tan", "log"]
        ]

        grid = QGridLayout()
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                button = QPushButton(btn_text)
                button.setStyleSheet(f"font-size: 24px; padding: 20px; background: {SECONDARY_COLOR};")
                grid.addWidget(button, row_idx, col_idx)
        layout.addLayout(grid)

        # 工具栏
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # 主题切换
        self.theme_menu = QComboBox()
        self.theme_menu.addItems(["Dark Theme", "Light Theme"])
        toolbar.addWidget(self.theme_menu)

        # 历史记录面板
        self.history_list = QListWidget()
        self.history_list.setVisible(False)
        layout.addWidget(self.history_list)

        # 绑定图标
        history_action = QAction(QIcon("assets/icons/history.png"), "History", self)
        toolbar.addAction(history_action)