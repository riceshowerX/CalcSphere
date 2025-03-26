import numexpr as ne
from math import sin, cos, tan, log10

class CalculatorModel:
    def calculate(self, expression: str) -> str:
        try:
            # 替换符号并安全计算
            sanitized = expression.replace("^", "**")
            result = ne.evaluate(sanitized).item()
            return str(result)
        except Exception as e:
            return "Error"