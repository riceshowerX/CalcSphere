from app.model import CalculatorModel
from app.utils import HistoryManager
from PyQt6.QtWidgets import QPushButton, QListWidgetItem  # 仅保留 QtWidgets 组件
from PyQt6.QtGui import QShortcut, QKeySequence          # 明确从 QtGui 导入
from PyQt6.QtCore import Qt
import traceback

class CalculatorController:
    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel()
        self.history = HistoryManager()
        self.load_history()  # 启动时加载历史记录
        self.connect_signals()
        self.bind_keyboard_shortcuts()  # 新增键盘支持

    def connect_signals(self):
        """优化信号连接逻辑"""
        # 使用 partial 避免闭包问题
        for btn in self.view.findChildren(QPushButton):
            btn.clicked.connect(lambda _, text=btn.text(): self.handle_input(text))
        
        self.view.theme_menu.currentTextChanged.connect(self.change_theme)
        self.view.history_list.itemClicked.connect(self.load_history_item)
        self.view.display.returnPressed.connect(self.handle_equal)  # 支持回车键计算

    def handle_input(self, text):
        """增强输入处理逻辑"""
        current = self.view.display.text().strip()
        
        if text == "=":
            self.handle_equal()
        elif text == "C":
            self.view.display.clear()
        elif text == "←":  # 新增退格功能
            self.view.display.setText(current[:-1])
        else:
            # 输入验证：防止连续运算符等非法输入
            if self.is_valid_input(current, text):
                self.view.display.setText(current + text)

    def handle_equal(self):
        """独立计算逻辑"""
        expression = self.view.display.text().strip()
        if not expression:
            return
            
        try:
            result = self.model.calculate(expression)
            self.view.display.setText(result)
            self.history.add(f"{expression} = {result}")
            self.save_history()  # 实时保存历史记录
        except Exception as e:
            self.view.display.setText(f"错误：{str(e)}")
            print(traceback.format_exc())

    def is_valid_input(self, current: str, new_char: str) -> bool:
        """新增输入验证规则"""
        # 防止重复运算符
        if new_char in "+-*/^" and current.endswith(("+", "-", "*", "/", "^")):
            return False
            
        # 防止括号不匹配（简单检测）
        if new_char == ")" and current.count("(") <= current.count(")"):
            return False
            
        return True

    def change_theme(self, theme_name: str):
        """增强主题切换稳定性"""
        try:
            with open(f"assets/styles/{theme_name.lower().replace(' ', '_')}.qss", "r") as f:
                self.view.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"警告：主题文件 {theme_name} 未找到，使用默认样式")
            self.view.setStyleSheet("")  # 重置样式

    def load_history_item(self, item: QListWidgetItem):
        """优化历史记录加载"""
        full_expression = item.text().split(" = ")[0]
        self.view.display.setText(full_expression)
        # 自动触发计算（可选）
        # self.handle_equal()

    def bind_keyboard_shortcuts(self):
        """新增键盘快捷键支持"""
        self.view.display.setPlaceholderText("输入表达式 (支持键盘操作)")
        
        # 绑定数字和运算符
        for key in "0123456789+-*/.^()":
            QShortcut(QKeySequence(key), self.view, 
                     lambda k=key: self.handle_input(k))
        
        # 绑定回退键
        QShortcut(QKeySequence(Qt.Key.Key_Backspace), self.view, 
                 lambda: self.handle_input("←"))
        QShortcut(QKeySequence(Qt.Key.Key_Enter), self.view, self.handle_equal)
        QShortcut(QKeySequence(Qt.Key.Key_Return), self.view, self.handle_equal)

    def load_history(self):
        """从文件加载历史记录"""
        self.history.load_from_file()
        self.view.history_list.addItems(self.history.get_all())

    def save_history(self):
        """实时保存历史记录"""
        self.history.save_to_file()