from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RESCENE - Deja Vu (Official Color Coded)</title>
    <style>
        body {
            background-color: #161616;
            color: #ffffff;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .terminal-box {
            background-color: #0d0d0d;
            border: 1px solid #2d2d2d;
            border-radius: 12px;
            padding: 25px;
            width: 85%;
            max-width: 650px;
            height: 70vh;
            overflow-y: auto;
            box-shadow: 0 15px 35px rgba(0,0,0,0.7);
            scroll-behavior: smooth;
        }

        /* ตกแต่งชื่อเพลงด้านบนกล่อง */
        .song-title {
            font-size: 26px;
            font-weight: bold;
            color: #ffffff;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-align: center;
        }

        .terminal-box::-webkit-scrollbar {
            width: 6px;
        }
        .terminal-box::-webkit-scrollbar-thumb {
            background-color: #333;
            border-radius: 4px;
        }

        .line {
            margin-bottom: 12px;
            white-space: pre-wrap;
            font-size: 18px;
            font-weight: bold;
            line-height: 1.5;
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

    <div class="terminal-box">
        <div class="song-title">🎵 Deja Vu - RESCENE</div>
        
        <div id="code-container"></div>
    </div>

    <script>
        // โค้ดสีประจำตัวเมมเบอร์: Woni(#E07A9E) | Liv(#B47EE3) | Minami(#47CFC3) | May(#E5C564) | Zena(#EAA079)
        const codeLines = [
            { text: "햇살 젖은 바람 잠이 든 I", color: "#E07A9E" }, // Woni
            { text: "물든 창문 틈새", color: "#B47EE3" }, // Liv
            { text: "스며든 light", color: "#47CFC3" }, // Minami
            { text: "나의 코끝을 스친 scent", color: "#E5C564" }, // May
            { text: "(그 향기에)", color: "#EAA079" }, // Zena
            { text: "피어난 작은 보조개", color: "#E07A9E" }, // Woni
            { text: "(Oh It’s so bright)", color: "#B47EE3" }, // Liv
            { text: "", color: "#ffffff" },
            { text: "책상 위에 그린 낙서", color: "#47CFC3" }, // Minami
            { text: "너와 나눈 그 비밀도", color: "#E5C564" }, // May
            { text: "바람결에 실려 다시", color: "#EAA079" }, // Zena
            { text: "되돌아간 기분 after all", color: "#E07A9E" }, // Woni
            { text: "", color: "#ffffff" },
            { text: "처음 스친 그때", color: "#B47EE3" }, // Liv
            { text: "이 향길 기억해 줘", color: "#47CFC3" }, // Minami
            { text: "닿은 그 순간", color: "#E5C564" }, // May
            { text: "펼쳐질 deja vu", color: "#EAA079" }, // Zena
            { text: "같은 꿈을 꾸듯", color: "#E07A9E" }, // Woni
            { text: "눈을 감아보면", color: "#B47EE3" }, // Liv
            { text: "익숙한 deja vu", color: "#47CFC3" }, // Minami
            { text: "Oh oh oh ha", color: "#E5C564" }, // May
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#EAA079" }, // Zena
            { text: "Yeah it’s like a deja vu", color: "#E07A9E" }, // Woni
            { text: "You and I", color: "#B47EE3" }, // Liv
            { text: "다시 닿을 수 없다 해도", color: "#47CFC3" }, // Minami
            { text: "같은 꿈을 꾸듯", color: "#E5C564" }, // May
            { text: "눈을 감아보면", color: "#EAA079" }, // Zena
            { text: "익숙한 deja vu", color: "#E07A9E" }, // Woni
            { text: "Oh oh oh ha", color: "#B47EE3" }, // Liv
            { text: "", color: "#ffffff" },
            { text: "빽빽한 책장 사이", color: "#47CFC3" }, // Minami
            { text: "손때 묻은 한 칸", color: "#E5C564" }, // May
            { text: "바랜 책 모퉁일", color: "#EAA079" }, // Zena
            { text: "넘기면 튀어나온", color: "#E07A9E" }, // Woni
            { text: "", color: "#ffffff" },
            { text: "자그만 이야길 들어", color: "#B47EE3" }, // Liv
            { text: "(귀 기울여 봐)", color: "#47CFC3" }, // Minami
            { text: "조금은 서툴렀던 날", color: "#E5C564" }, // May
            { text: "", color: "#ffffff" },
            { text: "빛이 바랜 쪽지 속에", color: "#EAA079" }, // Zena
            { text: "나를 어루만진 네 voice", color: "#E07A9E" }, // Woni
            { text: "바람결에 실려 다시", color: "#B47EE3" }, // Liv
            { text: "되돌아간 기분 after all", color: "#47CFC3" }, // Minami
            { text: "", color: "#ffffff" },
            { text: "처음 스친 그때", color: "#E5C564" }, // May
            { text: "이 향길 기억해 줘", color: "#EAA079" }, // Zena
            { text: "닿은 그 순간", color: "#E07A9E" }, // Woni
            { text: "펼쳐질 deja vu", color: "#B47EE3" }, // Liv
            { text: "같은 꿈을 꾸듯", color: "#47CFC3" }, // Minami
            { text: "눈을 감아보면", color: "#E5C564" }, // May
            { text: "익숙한 deja vu", color: "#EAA079" }, // Zena
            { text: "Oh oh oh ha", color: "#E07A9E" }, // Woni
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#B47EE3" }, // Liv
            { text: "Yeah it’s like a deja vu", color: "#47CFC3" }, // Minami
            { text: "You and I", color: "#E5C564" }, // May
            { text: "다시 닿을 수 없다 해도", color: "#EAA079" }, // Zena
            { text: "같은 꿈을 꾸듯", color: "#E07A9E" }, // Woni
            { text: "눈을 감아보면", color: "#B47EE3" }, // Liv
            { text: "익숙한 deja vu", color: "#47CFC3" }, // Minami
            { text: "Oh oh oh ha", color: "#E5C564" }, // May
            { text: "", color: "#ffffff" },
            { text: "(I’ve been thinking about you)", color: "#EAA079" }, // Zena
            { text: "그리워질 너와 나", color: "#E07A9E" }, // Woni
            { text: "(I’ve been dreaming about you)", color: "#B47EE3" }, // Liv
            { text: "이 순간을 잊지 마", color: "#47CFC3" }, // Minami
            { text: "", color: "#ffffff" },
            { text: "언젠가", color: "#E5C564" }, // May
            { text: "세상 끝해서", color: "#EAA079" }, // Zena
            { text: "마주할 날", color: "#E07A9E" }, // Woni
            { text: "오랜 deja vu", color: "#B47EE3" }, // Liv
            { text: "같은 꿈을 꾸듯", color: "#47CFC3" }, // Minami
            { text: "눈을 감아보면", color: "#E5C564" }, // May
            { text: "익숙한 deja vu", color: "#EAA079" }, // Zena
            { text: "Oh oh oh ha", color: "#E07A9E" }, // Woni
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#B47EE3" }, // Liv
            { text: "Yeah it’s like a deja vu", color: "#47CFC3" }, // Minami
            { text: "You and I", color: "#E5C564" }, // May
            { text: "다시 닿을 수 없다 해도", color: "#EAA079" }, // Zena
            { text: "같은 꿈을 꾸듯", color: "#E07A9E" }, // Woni
            { text: "눈을 감아보면", color: "#B47EE3" }, // Liv
            { text: "익숙한 deja vu", color: "#47CFC3" }, // Minami
            { text: "Oh oh oh ha", color: "#E5C564" }, // May
            { text: "", color: "#ffffff" },
            
            // --- พาร์ท Romanization ---
            { text: "haessal jeojeun baram jami deun I", color: "#E07A9E" },
            { text: "muldeun changmun teumsae", color: "#B47EE3" },
            { text: "seumyeodeun light", color: "#47CFC3" },
            { text: "naui kokkeuteul seuchin scent", color: "#E5C564" },
            { text: "(geu hyanggie)", color: "#EAA079" },
            { text: "pieonan jageun bojogae", color: "#E07A9E" },
            { text: "(Oh It’s so bright)", color: "#B47EE3" },
            { text: "", color: "#ffffff" },
            { text: "chaeksang wie geurin nakseo", color: "#47CFC3" },
            { text: "neowa nanun geu bimildo", color: "#E5C564" },
            { text: "baramgyeore sillyeo dasi", color: "#EAA079" },
            { text: "doedoragan gibun after all", color: "#E07A9E" },
            { text: "", color: "#ffffff" },
            { text: "cheoeum seuchin geuttae", color: "#B47EE3" },
            { text: "i hyanggil gieokhae jwo", color: "#47CFC3" },
            { text: "daheun geu sungan", color: "#E5C564" },
            { text: "pyeolchyeojil deja vu", color: "#EAA079" },
            { text: "gateun kkumeul kkudeut", color: "#E07A9E" },
            { text: "nuneul gamabomyeon", color: "#B47EE3" },
            { text: "iksukhan deja vu", color: "#47CFC3" },
            { text: "Oh oh oh ha", color: "#E5C564" },
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#EAA079" },
            { text: "Yeah it’s like a deja vu", color: "#E07A9E" },
            { text: "You and I", color: "#B47EE3" },
            { text: "dasi daheul su eopsda haedo", color: "#47CFC3" },
            { text: "gateun kkumeul kkudeut", color: "#E5C564" },
            { text: "nuneul gamabomyeon", color: "#EAA079" },
            { text: "iksukhan deja vu", color: "#E07A9E" },
            { text: "Oh oh oh ha", color: "#B47EE3" },
            { text: "", color: "#ffffff" },
            { text: "ppaekppaekhan chaekjang sai", color: "#47CFC3" },
            { text: "sonttae mudeun han kan", color: "#E5C564" },
            { text: "baraen chaek motungil", color: "#EAA079" },
            { text: "neomgimyeon twieonaon", color: "#E07A9E" },
            { text: "", color: "#ffffff" },
            { text: "jageuman iyagil deureo", color: "#B47EE3" },
            { text: "(gwi giuryeo bwa)", color: "#47CFC3" },
            { text: "jogeumeun seotulleossdeon nal", color: "#E5C564" },
            { text: "", color: "#ffffff" },
            { text: "bicci baraen jjokji soge", color: "#EAA079" },
            { text: "nareul eorumanjin ne voice", color: "#E07A9E" },
            { text: "baramgyeore sillyeo dasi", color: "#B47EE3" },
            { text: "doedoragan gibun after all", color: "#47CFC3" },
            { text: "", color: "#ffffff" },
            { text: "cheoeum seuchin geuttae", color: "#E5C564" },
            { text: "i hyanggil gieokhae jwo", color: "#EAA079" },
            { text: "daheun geu sungan", color: "#E07A9E" },
            { text: "pyeolchyeojil deja vu", color: "#B47EE3" },
            { text: "gateun kkumeul kkudeut", color: "#47CFC3" },
            { text: "nuneul gamabomyeon", color: "#E5C564" },
            { text: "iksukhan deja vu", color: "#EAA079" },
            { text: "Oh oh oh ha", color: "#E07A9E" },
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#B47EE3" },
            { text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { text: "You and I", color: "#E5C564" },
            { text: "dasi daheul su eopsda haedo", color: "#EAA079" },
            { text: "gateun kkumeul kkudeut", color: "#E07A9E" },
            { text: "nuneul gamabomyeon", color: "#B47EE3" },
            { text: "iksukhan deja vu", color: "#47CFC3" },
            { text: "Oh oh oh ha", color: "#E5C564" },
            { text: "", color: "#ffffff" },
            { text: "(I’ve been thinking about you)", color: "#EAA079" },
            { text: "geuriwojil neowa na", color: "#E07A9E" },
            { text: "(I’ve been dreaming about you)", color: "#B47EE3" },
            { text: "i sunganeul ijji ma", color: "#47CFC3" },
            { text: "", color: "#ffffff" },
            { text: "eonjenga", color: "#E5C564" },
            { text: "sesang kkeuteseo", color: "#EAA079" },
            { text: "majuhal nal", color: "#E07A9E" },
            { text: "oraen deja vu", color: "#B47EE3" },
            { text: "gateun kkumeul kkudeut", color: "#47CFC3" },
            { text: "nuneul gamabomyeon", color: "#E5C564" },
            { text: "iksukhan deja vu", color: "#EAA079" },
            { text: "Oh oh oh ha", color: "#E07A9E" },
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#B47EE3" },
            { text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { text: "You and I", color: "#E5C564" },
            { text: "dasi daheul su eopsda haedo", color: "#EAA079" },
            { text: "gateun kkumeul kkudeut", color: "#E07A9E" },
            { text: "nuneul gamabomyeon", color: "#B47EE3" },
            { text: "iksukhan deja vu", color: "#47CFC3" },
            { text: "Oh oh oh ha", color: "#E5C564" }
        ];

        const container = document.getElementById('code-container');
        const mainBox = document.querySelector('.terminal-box'); // ดึงตัวกล่องใหญ่มาเพื่อสั่งสกรอลล์ลงล่าง
        const typingSpeed = 40; 
        const lineDelay = 400;   

        const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        async function runCodeAnimation() {
            while (true) {
                container.innerHTML = ''; 
                
                for (let i = 0; i < codeLines.length; i++) {
                    const lineData = codeLines[i];
                    
                    const lineElement = document.createElement('div');
                    lineElement.className = 'line cursor';
                    lineElement.style.color = lineData.color;
                    container.appendChild(lineElement);

                    if(lineData.text === "") {
                        lineElement.innerHTML = "&nbsp;"; 
                        lineElement.classList.remove('cursor');
                        mainBox.scrollTop = mainBox.scrollHeight;
                        await sleep(lineDelay);
                        continue;
                    }

                    for (let char of lineData.text) {
                        lineElement.textContent += char;
                        mainBox.scrollTop = mainBox.scrollHeight;
                        await sleep(typingSpeed);
                    }

                    lineElement.classList.remove('cursor');
                    await sleep(lineDelay);
                }
                
                // รอเป็นเวลา 5 วินาทีก่อนที่จะเคลียร์หน้าจอแล้ววนรอบใหม่
                await sleep(5000); 
            }
        }

        window.onload = runCodeAnimation;
    </script>
</body>
</html>
"""

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

if __name__ == '__main__':
  app.run(debug=True)
