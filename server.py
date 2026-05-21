from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
  return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RESCENE - Deja Vu (Render Local Audio)</title>
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
            position: relative;
        }

        .start-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(22, 22, 22, 0.95);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 999;
            transition: opacity 0.5s ease;
        }

        .start-btn {
            background-color: #E07A9E;
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(224, 122, 158, 0.5);
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

        .song-title {
            font-size: 26px;
            font-weight: bold;
            color: #ffffff;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-align: center;
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

        @keyframes blink { 50% { opacity: 0; } }
    </style>
</head>
<body>

    <div class="start-overlay" id="overlay">
        <button class="start-btn" onclick="startEverything()">▶ Play Deja Vu</button>
    </div>

    <audio id="bg-music" loop>
        <source src="/get_music" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>

    <div class="terminal-box">
        <div class="song-title">🎵 Deja Vu - RESCENE</div>
        <div id="code-container"></div>
    </div>

    <script>
        const codeLines = [
            { text: "햇살 젖은 바람 잠이 든 I", color: "#E07A9E" },
            { text: "물든 창문 틈새", color: "#B47EE3" },
            { text: "스며든 light", color: "#47CFC3" },
            { text: "나의 코끝을 스친 scent", color: "#E5C564" },
            { text: "(그 향기에)", color: "#EAA079" },
            { text: "피어난 작은 보조개", color: "#E07A9E" },
            { text: "(Oh It’s so bright)", color: "#B47EE3" },
            { text: "", color: "#ffffff" },
            { text: "책상 위에 그린 낙서", color: "#47CFC3" }, 
            { text: "너와 나눈 그 비밀도", color: "#E5C564" }, 
            { text: "바람결에 실려 다시", color: "#EAA079" }, 
            { text: "되돌아간 기분 after all", color: "#E07A9E" }, 
            { text: "", color: "#ffffff" },
            { text: "처음 스친 그때", color: "#B47EE3" }, 
            { text: "이 향길 기억해 줘", color: "#47CFC3" }, 
            { text: "닿은 그 순간", color: "#E5C564" }, 
            { text: "펼쳐질 deja vu", color: "#EAA079" }, 
            { text: "같은 꿈을 꾸듯", color: "#E07A9E" }, 
            { text: "눈을 감아보면", color: "#B47EE3" }, 
            { text: "익숙한 deja vu", color: "#47CFC3" }, 
            { text: "Oh oh oh ha", color: "#E5C564" }, 
            { text: "", color: "#ffffff" },
            { text: "I I I I I", color: "#EAA079" }, 
            { text: "Yeah it’s like a deja vu", color: "#E07A9E" }, 
            { text: "You and I", color: "#B47EE3" }, 
            { text: "다시 닿을 수 없다 해도", color: "#47CFC3" }, 
            { text: "같은 꿈을 꾸듯", color: "#E5C564" }, 
            { text: "눈을 감아보면", color: "#EAA079" }, 
            { text: "익숙한 deja vu", color: "#E07A9E" }, 
            { text: "Oh oh oh ha", color: "#B47EE3" }
        ];

        const container = document.getElementById('code-container');
        const mainBox = document.querySelector('.terminal-box'); 
        const typingSpeed = 40; 
        const lineDelay = 400;   

        const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        function startEverything() {
            document.getElementById('overlay').style.opacity = '0';
            setTimeout(() => { document.getElementById('overlay').style.display = 'none'; }, 500);

            const music = document.getElementById('bg-music');
            music.play().catch(error => console.log("Playback error:", error));

            runCodeAnimation();
        }

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
                await sleep(5000); 
            }
        }
    </script>
</body>
</html>
"""

# ฟังก์ชัน Backend ดึงไฟล์เพลงในตัวเซิร์ฟเวอร์ Render ออกไปให้เบราว์เซอร์เล่น
@app.route('/get_music')
def get_music():
    return send_from_directory(os.getcwd(), 'music.mp3')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
