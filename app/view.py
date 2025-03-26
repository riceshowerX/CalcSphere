from PyQt6.QtWidgets import (
    QMainWindow, QLineEdit, QGridLayout, QPushButton, QWidget,
    QToolBar, QComboBox, QListWidget, QVBoxLayout, QSizePolicy
)
from PyQt6.QtGui import QAction, QIcon, QColor, QPalette, QFont
from PyQt6.QtCore import Qt, QSize
from config.constants import PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR
import math

class CalculatorView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CalcSphere")
        self.setGeometry(100, 100, 480, 720)
        self.setMinimumSize(360, 540)
        self.initUI()

    def initUI(self):
        # 主容器
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # 显示屏
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Segoe UI", 24))
        self.display.setStyleSheet(f"""
            QLineEdit {{
                background: {PRIMARY_COLOR};
                color: white;
                border-radius: 15px;
                padding: 20px;
                font-weight: 500;
                border: 2px solid {ACCENT_COLOR};
            }}
        """)
        layout.addWidget(self.display)

        # 科学计算按钮布局
        self.create_scientific_buttons(layout)

        # 数字和操作符布局
        self.create_main_buttons(layout)

        # 工具栏
        self.create_toolbar()

        # 历史记录面板
        self.create_history_panel(layout)

        # 应用样式
        self.apply_theme("Dark Theme")

    def create_scientific_buttons(self, layout):
        """创建科学计算按钮行"""
        scientific_layout = QGridLayout()
        scientific_layout.setSpacing(8)
        
        buttons = [
            ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2),
            ("ln", 1, 0), ("log", 1, 1), ("√", 1, 2),
            ("π", 2, 0), ("e", 2, 1), ("x²", 2, 2),
            ("(", 3, 0), (")", 3, 1), ("C", 3, 2)
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setFont(QFont("Segoe UI", 14))
            btn.setFixedSize(80, 60)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {SECONDARY_COLOR};
                    color: white;
                    border-radius: 12px;
                }}
                QPushButton:hover {{
                    background: {ACCENT_COLOR};
                }}
                QPushButton:pressed {{
                    background: {PRIMARY_COLOR};
                }}
            """)
            scientific_layout.addWidget(btn, row, col)
        
        layout.addLayout(scientific_layout)

    def create_main_buttons(self, layout):
        """创建数字和主要操作符布局"""
        main_layout = QGridLayout()
        main_layout.setSpacing(12)
        
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "=", "+"]
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = QPushButton(btn_text)
                btn.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
                btn.setFixedSize(90, 90)
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background: {SECONDARY_COLOR};
                        color: white;
                        border-radius: 45px;
                        border: 2px solid {ACCENT_COLOR};
                    }}
                    QPushButton:hover {{
                        background: {ACCENT_COLOR};
                        transform: scale(1.05);
                    }}
                    QPushButton:pressed {{
                        background: {PRIMARY_COLOR};
                    }}
                """)
                main_layout.addWidget(btn, row_idx, col_idx)
        
        layout.addLayout(main_layout)

    def create_toolbar(self):
        """创建顶部工具栏"""
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # 主题切换
        self.theme_menu = QComboBox()
        self.theme_menu.addItems(["Dark Theme", "Light Theme", "Dracula Theme"])
        self.theme_menu.setStyleSheet(f"""
            QComboBox {{
                background: {SECONDARY_COLOR};
                color: white;
                border-radius: 8px;
                padding: 8px;
            }}
        """)
        toolbar.addWidget(self.theme_menu)

        # 历史记录按钮
        history_action = QAction(QIcon("assets/icons/history.svg"), "History", self)
        history_action.setIconText("History")
        toolbar.addAction(history_action)

    def create_history_panel(self, layout):
        """创建历史记录面板"""
        self.history_list = QListWidget()
        self.history_list.setVisible(False)
        self.history_list.setStyleSheet(f"""
            QListWidget {{
                background: {SECONDARY_COLOR};
                color: white;
                border-radius: 15px;
                padding: 10px;
            }}
            QListWidget::item {{
                padding: 8px;
                border-bottom: 1px solid {ACCENT_COLOR};
            }}
            QListWidget::item:selected {{
                background: {ACCENT_COLOR};
            }}
        """)
        layout.addWidget(self.history_list)

    def apply_theme(self, theme_name):
        """应用主题样式"""
        palette = self.palette()
        
        if theme_name == "Dark Theme":
            palette.setColor(QPalette.ColorRole.Window, QColor("#2D2D2D"))
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            PRIMARY_COLOR = "#2D2D2D"
            SECONDARY_COLOR = "#4A4A4A"
            ACCENT_COLOR = "#007BFF"
        elif theme_name == "Light Theme":
            palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
            PRIMARY_COLOR = "#F5F5F5"
            SECONDARY_COLOR = "#E0E0E0"
            ACCENT_COLOR = "#007BFF"
        elif theme_name == "Dracula Theme":
            palette.setColor(QPalette.ColorRole.Window, QColor("#282A36"))
            palette.setColor(QPalette.ColorRole.Text, QColor("#F8F8F2"))
            PRIMARY_COLOR = "#282A36"
            SECONDARY_COLOR = "#44475A"
            ACCENT_COLOR = "#BD93F9"
        
        self.setPalette(palette)
        self.refresh_stylesheet(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)

    def refresh_stylesheet(self, primary, secondary, accent):
        """动态更新样式表"""
        self.setStyleSheet(f"""
            QMainWindow {{
                background: {primary};
            }}
            QPushButton {{
                background: {secondary};
                color: {self.get_text_color(secondary)};
            }}
        """)
        self.display.setStyleSheet(f"""
            QLineEdit {{
                background: {primary};
                color: {self.get_text_color(primary)};
                border: 2px solid {accent};
            }}
        """)

    def get_text_color(self, background):
        """根据背景色自动计算文字颜色"""
        luminance = QColor(background).lightness()
        return Qt.GlobalColor.white if luminance < 128 else Qt.GlobalColor.black