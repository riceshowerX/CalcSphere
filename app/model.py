import numexpr as ne
import math
import re

class CalculatorModel:
    CONSTANTS = {
        'pi': math.pi,
        'e': math.e,
        'tau': math.tau
    }

    def __init__(self):
        self.safe_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'abs': abs,
            'rad': math.radians,
            'deg': math.degrees
        }

    def calculate(self, expression: str) -> str:
        try:
            sanitized = self._sanitize_expression(expression)
            result = self._evaluate_expression(sanitized)
            return self._format_result(result)
            
        except ZeroDivisionError:
            return "错误：除数不能为零"
        except ValueError as ve:
            return f"错误：{ve}"
        except SyntaxError:
            return "错误：表达式格式错误"
        except Exception as e:
            print(f"未知错误：{str(e)}")
            return "错误：无法计算表达式"

    def _sanitize_expression(self, expr: str) -> str:
        # 替换运算符
        expr = expr.replace('^', '**')
        expr = expr.replace(',', '.')
        
        # 替换常量
        for const, value in self.CONSTANTS.items():
            expr = re.sub(rf'\b{const}\b', str(value), expr, flags=re.IGNORECASE)
        
        # 验证表达式安全性
        if not self._is_expression_safe(expr):
            raise ValueError("检测到非法字符")
            
        return expr

    def _evaluate_expression(self, expr: str):
        # 优先使用 numexpr 计算
        try:
            return ne.evaluate(expr, local_dict=self.safe_functions).item()
        except:
            # 处理更复杂的数学函数
            return eval(expr, {'__builtins__': None}, self.safe_functions)

    def _format_result(self, value: float) -> str:
        if isinstance(value, complex):
            return f"{value.real:.4f} + {value.imag:.4f}i"
            
        if abs(value) < 1e-10:
            return "0"
            
        if abs(value) > 1e10:
            return f"{value:.4e}"
            
        return f"{value:.10f}".rstrip('0').rstrip('.') if '.' in f"{value}" else f"{value}"

    def _is_expression_safe(self, expr: str) -> bool:
        # 允许的字符：数字、运算符、括号、小数点、函数名
        allowed_pattern = re.compile(r'^[0-9+\-*/().^% \t\w]+$')
        return allowed_pattern.match(expr) is not None