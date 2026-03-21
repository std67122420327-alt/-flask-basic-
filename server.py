from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask Basic</title>
</head>
<body>
  <h1>Hui Senมาแล้วจ้า</h1>
  <hr>
</body>
</html>"""

@app.route('/user/<name>/<age>')
def my_name(name, age):
  return f'<h1> My name is {name}.I\'m {age+1} years old.</h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a,b):
  return f'<h1>{a} + {b} = {a+b}<h1>'

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def subtraction(a,b):
  return f'<h1>{a} - {b} = {a-b}<h1>'

@app.route('/calculator/multiplication/<int:a>/<int:b>')
def multiplication(a,b):
  return f'<h1>{a} * {b} = {a*b}<h1>'

@app.route('/calculator/division/<int:a>/<int:b>')
def division(a,b):
  return f'<h1>{a} / {b} = {a/b}<h1>'

@app.route('/calculator/mod/<int:a>/<int:b>')
def mod(a,b):
  return f'<h1>{a} % {b} = {a%b}<h1>'

@app.route('/calculator/power/<float:base>/<float:exponent>')
def power(base,exponent):
  return f'<h1>{base} <sup> {base} </sup> = {base**exponent}<h1>'

@app.route('/calculator/div/<int:a>/<int:b>')
def div(a, b):
  return f'<h1>{a} // {b} = {a//b}</h1>'



#if __name__ == '__main__':
# app.route()
