
from flask import Flask, render_template, request

app = Flask(__name__)

# Safe evaluator for math expressions
ALLOWED_CHARS = set("0123456789+-*/(). ^")

def calculate(expression: str) -> str:
    try:
        expr = expression.replace('×', '*').replace('÷', '/').replace('^', '**')

        if not expr.strip():
            return ''

        for c in expr:
            if c not in ALLOWED_CHARS and c != ' ':
                return 'Error: invalid character'

        # Use eval in controlled environment.
        result = eval(expr, {'__builtins__': None}, {})
        return str(result)
    except ZeroDivisionError:
        return 'Error: division by zero'
    except Exception:
        return 'Error'

@app.route('/', methods=['GET', 'POST'])
def index():
    expr = ''
    result = ''
    if request.method == 'POST':
        expr = request.form.get('expression', '')
        if expr:
            result = calculate(expr)
    return render_template('calculator.html', expression=expr, result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

