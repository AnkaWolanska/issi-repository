"""This is simple calculator"""

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/calculate')
def calculate():
    """Perform calculations"""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    if op == 'sum':
        return f"{arg1} + {arg2} = {arg1+arg2}"
    if op == 'sub':
        return f"{arg1} - {arg2} = {arg1-arg2}"
    if op == 'mul':
        return f"{arg1} * {arg2} = {arg1*arg2}"
    if op == 'div':
        if arg2 == 0:
            return "Don't divide by 0"
        return f"{arg1} / {arg2} = {arg1/arg2}"
    return f"invalid operation: {op}"

if __name__ == '__main__':
    app.run()
