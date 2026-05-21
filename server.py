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
    <title>RESCENE - Deja Vu (Render Server)</title>
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
        <source src="https://pub-2f92d4a3ca0c497cae9e03d3de19d9c2.r2.dev/RESCENE_Deja_Vu.mp3" type="audio/mpeg">
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
            { text: "(Oh It’s so bright)", color: "#B47EE3" }
        ];

        const container = document.getElementById('code-container');
        const mainBox = document.querySelector('.terminal-box'); 
        const typingSpeed = 40; 
        const lineDelay = 400;   

        const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        function startEverything() {
            document.getElementById('overlay').style.display = 'none';
            const music = document.getElementById('bg-music');
            music.play().catch(error => console.log(error));
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

if __name__ == '__main__':
    app.run(debug=True)
