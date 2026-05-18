from flask import Flask

app = Flask(__name__)

# หน้าแรก: ดึงโค้ดแอนิเมชันแก๊งเด็กดื้อสีเขียวมาแสดงผล
@app.route('/')
def index():
  return """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แก๊งเด็กดื้อ - Green Edition</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .terminal-box {
            background-color: #181818;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 30px;
            width: 80%;
            max-width: 500px;
            min-height: 180px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .line {
            margin-bottom: 15px;
            white-space: pre;
            font-size: 24px;
            font-weight: bold;
        }

        .cursor::after {
            content: "█";
            animation: blink 0.6s infinite;
            margin-left: 5px;
        }

        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
</head>
<body>

    <div class="terminal-box" id="code-container">
        </div>

    <script>
        const codeLines = [
            { text: "น้องอชิ", color: "#55efc4" },  
            { text: "น้องอลิส", color: "#2ecc71" }, 
            { text: "เด็กดื้อ", color: "#98c379" }   
        ];

        const container = document.getElementById('code-container');
        const typingSpeed = 100; 
        const lineDelay = 600;   

        const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        async function runCodeAnimation() {
            for (let i = 0; i < codeLines.length; i++) {
                const lineData = codeLines[i];
                
                const lineElement = document.createElement('div');
                lineElement.className = 'line cursor';
                lineElement.style.color = lineData.color;
                container.appendChild(lineElement);

                for (let char of lineData.text) {
                    lineElement.textContent += char;
                    await sleep(typingSpeed);
                }

                lineElement.classList.remove('cursor');
                await sleep(lineDelay);
            }
        }

        window.onload = runCodeAnimation;
    </script>
</body>
</html>
"""

# แก้ไขเพิ่ม <int:age> เพื่อให้ระบบรู้ว่าเป็นตัวเลขและคำนวณ {age+1} ได้
@app.route('/user/<name>/<int:age>')
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
  return f'<h1>{base} <sup> {exponent} </sup> = {base**exponent}<h1>'

@app.route('/calculator/div/<int:a>/<int:b>')
def div(a, b):
  return f'<h1>{a} // {b} = {a//b}</h1>'

# เปิดคอมเมนต์เพื่อให้สั่งรันโปรแกรมได้
if __name__ == '__main__':
  app.run(debug=True)
