#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string_param>')
def print_string(string_param):
    print(string_param)
    return string_param  

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = '\n'.join(str(i) for i in range(1, int_param + 1))
    return numbers  

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div': 
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    app.run(debug=True)