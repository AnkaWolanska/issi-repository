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
    if op == '+':
        return f"{arg1} + {arg2} = {arg1+arg2}"
    if op == '-':
        return f"{arg1} - {arg2} = {arg1-arg2}"
    if op == '*':
        return f"{arg1} * {arg2} = {arg1*arg2}"
    return f"invalid operation: {op}"

if __name__ == '__main__':
    app.run()
