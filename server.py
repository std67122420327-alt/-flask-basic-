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
    <title>RESCENE - Deja Vu (Full Sync Lyrics & Controls)</title>
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
            overflow: hidden;
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
            position: relative;
        }

        .terminal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #333;
            padding-bottom: 15px;
            margin-bottom: 20px;
            position: sticky;
            top: 0;
            background-color: #0d0d0d;
            z-index: 10;
        }

        .song-title {
            font-size: 22px;
            font-weight: bold;
            color: #ffffff;
            margin: 0;
        }

        .audio-controls {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .control-btn {
            background-color: #222;
            color: #fff;
            border: 1px solid #444;
            padding: 6px 14px;
            font-size: 14px;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
            transition: all 0.2s;
        }

        .control-btn:hover {
            background-color: #E07A9E;
            border-color: #E07A9E;
        }

        .time-display {
            font-size: 16px;
            color: #888;
            font-weight: bold;
            background: #1a1a1a;
            padding: 4px 10px;
            border-radius: 6px;
            border: 1px solid #2d2d2d;
        }

        .line {
            margin-bottom: 12px;
            white-space: pre-wrap;
            font-size: 19px;
            font-weight: bold;
            line-height: 1.6;
            opacity: 0.2;
            transition: opacity 0.3s;
        }

        .line.active {
            opacity: 1;
            filter: drop-shadow(0 0 4px var(--line-color));
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

    <div class="terminal-box" id="terminal">
        <div class="terminal-header">
            <h1 class="song-title">🎵 Deja Vu - RESCENE</h1>
            <div class="audio-controls">
                <div class="time-display" id="time-viewer">00:00</div>
                <button class="control-btn" id="play-pause-btn" onclick="togglePlayPause()">⏸ Pause</button>
            </div>
        </div>
        <div id="code-container"></div>
    </div>

    <script>
        // โค้ดสีประจำตัวเมมเบอร์: Woni(#E07A9E) | Liv(#B47EE3) | Minami(#47CFC3) | May(#E5C564) | Zena(#EAA079)
        // รวมเนื้อเพลงทั้งหมดครบ 100% ตัวเต็ม
        const codeLines = [
            // ==========================================
            // KOREAN VERSION
            // ==========================================
            { time: 9.0, text: "햇살 젖은 바람 잠이 든 I", color: "#E07A9E" },
            { time: 13.0, text: "물든 창문 틈새 스며든 light", color: "#B47EE3" },
            { time: 16.0, text: "나의 코끝을 스친 scent", color: "#47CFC3" },
            { time: 19.5, text: "(그 향기에)", color: "#EAA079" },
            { time: 22.0, text: "피어난 작은 보조개", color: "#E07A9E" },
            { time: 25.5, text: "(Oh It’s so bright)", color: "#B47EE3" },
            { time: 28.0, text: "", color: "#ffffff" },
            
            { time: 28.5, text: "책상 위에 그린 낙서", color: "#47CFC3" },
            { time: 32.0, text: "너와 나눈 그 비밀도", color: "#E5C564" },
            { time: 35.5, text: "바람결에 실려 다시", color: "#EAA079" },
            { time: 39.0, text: "되돌아간 기분 after all", color: "#E07A9E" },
            { time: 43.0, text: "", color: "#ffffff" },
            
            { time: 43.5, text: "처음 스친 그때 이 향길 기억해 줘", color: "#B47EE3" },
            { time: 50.5, text: "닿은 그 순간 펼쳐질 deja vu", color: "#47CFC3" },
            { time: 57.5, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#E5C564" },
            { time: 61.5, text: "익숙한 deja vu Oh oh oh ha", color: "#EAA079" },
            { time: 65.0, text: "", color: "#ffffff" },
            
            { time: 65.5, text: "I I I I I", color: "#EAA079" },
            { time: 68.0, text: "Yeah it’s like a deja vu", color: "#E07A9E" },
            { time: 72.0, text: "You and I", color: "#B47EE3" },
            { time: 74.0, text: "다시 닿을 수 없다 해도", color: "#47CFC3" },
            { time: 79.0, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#E5C564" },
            { time: 83.0, text: "익숙한 deja vu Oh oh oh ha", color: "#E07A9E" },
            { time: 86.5, text: "", color: "#ffffff" },
            
            { time: 87.0, text: "빽빽한 책장 사이 손때 묻은 한 칸", color: "#47CFC3" },
            { time: 90.5, text: "바랜 책 모퉁일 넘기면 튀어나온", color: "#E5C564" },
            { time: 94.0, text: "자그만 이야길 들어 (귀 기울여 봐)", color: "#B47EE3" },
            { time: 98.0, text: "조금은 서툴렀던 날", color: "#E07A9E" },
            { time: 101.0, text: "", color: "#ffffff" },
            
            { time: 101.5, text: "빛이 바랜 쪽지 속에 나를 어루만진 네 voice", color: "#EAA079" },
            { time: 105.0, text: "바람결에 실려 다시 되돌아간 기분 after all", color: "#E07A9E" },
            { time: 109.0, text: "", color: "#ffffff" },
            
            { time: 109.5, text: "처음 스친 그때 이 향길 기억해 줘", color: "#E5C564" },
            { time: 116.5, text: "닿은 그 순간 펼쳐질 deja vu", color: "#EAA079" },
            { time: 123.5, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#E07A9E" },
            { time: 127.5, text: "익숙한 deja vu Oh oh oh ha", color: "#B47EE3" },
            { time: 131.0, text: "", color: "#ffffff" },
            
            { time: 131.5, text: "I I I I I", color: "#B47EE3" },
            { time: 134.0, text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { time: 138.0, text: "You and I", color: "#E5C564" },
            { time: 140.0, text: "다시 닿을 수 없다 해도", color: "#EAA079" },
            { time: 145.0, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#E07A9E" },
            { time: 149.0, text: "익숙한 deja vu Oh oh oh ha", color: "#B47EE3" },
            { time: 152.5, text: "", color: "#ffffff" },
            
            { time: 153.0, text: "(I’ve been thinking about you)", color: "#EAA079" },
            { time: 156.0, text: "그리워질 너와 나", color: "#E07A9E" },
            { time: 160.0, text: "(I’ve been dreaming about you)", color: "#B47EE3" },
            { time: 163.0, text: "이 순간을 잊지 마", color: "#47CFC3" },
            { time: 166.5, text: "", color: "#ffffff" },
            
            { time: 167.0, text: "언젠가 세상 끝에서 마주할 날 오랜 deja vu", color: "#E5C564" },
            { time: 174.0, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#EAA079" },
            { time: 178.0, text: "익숙한 deja vu Oh oh oh ha", color: "#E07A9E" },
            { time: 181.5, text: "", color: "#ffffff" },
            
            { time: 182.0, text: "I I I I I", color: "#B47EE3" },
            { time: 184.5, text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { time: 188.5, text: "You and I", color: "#E5C564" },
            { time: 190.5, text: "다시 닿을 수 없다 해도", color: "#EAA079" },
            { time: 195.5, text: "같은 꿈을 꾸듯 눈을 감아보면", color: "#E07A9E" },
            { time: 199.5, text: "익숙한 deja vu Oh oh oh ha", color: "#B47EE3" },
            { time: 204.0, text: "", color: "#ffffff" },

            // ==========================================
            // ROMANIZATION VERSION
            // ==========================================
            { time: 205.0, text: "----------------------------------------", color: "#555555" },
            { time: 205.5, text: "          ROMANIZATION VERSION          ", color: "#ffffff" },
            { time: 206.0, text: "----------------------------------------", color: "#555555" },
            { time: 206.5, text: "", color: "#ffffff" },
            
            { time: 207.0, text: "haessal jeojeun baram jami deun I", color: "#E07A9E" },
            { time: 211.0, text: "muldeun changmun teumsae seumyeodeun light", color: "#B47EE3" },
            { time: 214.0, text: "naui kokkeuteul seuchin scent", color: "#47CFC3" },
            { time: 217.5, text: "(geu hyanggie)", color: "#EAA079" },
            { time: 219.0, text: "pieonan jageun bojogae", color: "#E07A9E" },
            { time: 222.0, text: "(Oh It’s so bright)", color: "#B47EE3" },
            { time: 225.0, text: "", color: "#ffffff" },
            
            { time: 225.5, text: "chaeksang wie geurin nakseo", color: "#47CFC3" },
            { time: 228.0, text: "neowa nanun geu bimildo", color: "#E5C564" },
            { time: 231.0, text: "baramgyeore sillyeo dasi", color: "#EAA079" },
            { time: 234.0, text: "doedoragan gibun after all", color: "#E07A9E" },
            { time: 237.5, text: "", color: "#ffffff" },
            
            { time: 238.0, text: "cheoeum seuchin geuttae i hyanggil gieokhae jwo", color: "#B47EE3" },
            { time: 243.5, text: "daheun geu sungan pyeolchyeojil deja vu", color: "#47CFC3" },
            { time: 249.5, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#E5C564" },
            { time: 254.0, text: "iksukhan deja vu Oh oh oh ha", color: "#EAA079" },
            { time: 258.0, text: "", color: "#ffffff" },
            
            { time: 258.5, text: "I I I I I", color: "#EAA079" },
            { time: 261.0, text: "Yeah it’s like a deja vu", color: "#E07A9E" },
            { time: 264.0, text: "You and I", color: "#B47EE3" },
            { time: 266.0, text: "dasi daheul su eopsda haedo", color: "#47CFC3" },
            { time: 271.0, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#E5C564" },
            { time: 275.0, text: "iksukhan deja vu Oh oh oh ha", color: "#E07A9E" },
            { time: 279.0, text: "", color: "#ffffff" },
            
            { time: 279.5, text: "ppaekppaekhan chaekjang sai sonttae mudeun han kan", color: "#47CFC3" },
            { time: 283.0, text: "baraen chaek motungil neomgimyeon twieonaon", color: "#E5C564" },
            { time: 286.5, text: "jageuman iyagil deureo (gwi giuryeo bwa)", color: "#B47EE3" },
            { time: 290.0, text: "jogeumeun seotulleossdeon nal", color: "#E07A9E" },
            { time: 293.0, text: "", color: "#ffffff" },
            
            { time: 293.5, text: "bicci baraen jjokji soge nareul eorumanjin ne voice", color: "#EAA079" },
            { time: 297.0, text: "baramgyeore sillyeo dasi doedoragan gibun after all", color: "#47CFC3" },
            { time: 301.5, text: "", color: "#ffffff" },
            
            { time: 302.0, text: "cheoeum seuchin geuttae i hyanggil gieokhae jwo", color: "#E5C564" },
            { time: 307.0, text: "daheun geu sungan pyeolchyeojil deja vu", color: "#EAA079" },
            { time: 313.0, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#E07A9E" },
            { time: 317.0, text: "iksukhan deja vu Oh oh oh ha", color: "#B47EE3" },
            { time: 321.0, text: "", color: "#ffffff" },
            
            { time: 321.5, text: "I I I I I", color: "#B47EE3" },
            { time: 324.0, text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { time: 327.5, text: "You and I", color: "#E5C564" },
            { time: 329.5, text: "dasi daheul su eopsda haedo", color: "#EAA079" },
            { time: 334.5, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#E07A9E" },
            { time: 338.5, text: "iksukhan deja vu Oh oh oh ha", color: "#B47EE3" },
            { time: 342.5, text: "", color: "#ffffff" },
            
            { time: 343.0, text: "(I’ve been thinking about you)", color: "#EAA079" },
            { time: 346.5, text: "geuriwojil neowa na", color: "#E07A9E" },
            { time: 350.0, text: "(I’ve been dreaming about you)", color: "#B47EE3" },
            { time: 353.5, text: "i sunganeul ijji ma", color: "#47CFC3" },
            { time: 357.0, text: "", color: "#ffffff" },
            
            { time: 357.5, text: "eonjenga sesang kkeuteseo majuhal nal oraen deja vu", color: "#E5C564" },
            { time: 364.5, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#EAA079" },
            { time: 368.5, text: "iksukhan deja vu Oh oh oh ha", color: "#E07A9E" },
            { time: 372.5, text: "", color: "#ffffff" },
            
            { time: 373.0, text: "I I I I I", color: "#B47EE3" },
            { time: 375.5, text: "Yeah it’s like a deja vu", color: "#47CFC3" },
            { time: 379.5, text: "You and I", color: "#E5C564" },
            { time: 381.5, text: "dasi daheul su eopsda haedo", color: "#EAA079" },
            { time: 386.5, text: "gateun kkumeul kkudeut nuneul gamabomyeon", color: "#E07A9E" },
            { time: 390.5, text: "iksukhan deja vu Oh oh oh ha", color: "#E5C564" }
        ];

        const container = document.getElementById('code-container');
        const terminal = document.getElementById('terminal');
        const music = document.getElementById('bg-music');
        const timeViewer = document.getElementById('time-viewer');
        const playPauseBtn = document.getElementById('play-pause-btn');
        let currentLineIndex = -1;

        function initLyrics() {
            container.innerHTML = '';
            codeLines.forEach((line, index) => {
                const div = document.createElement('div');
                div.className = 'line';
                div.id = `line-${index}`;
                div.style.setProperty('--line-color', line.color);
                div.style.color = line.color;
                container.appendChild(div);
            });
        }

        function startEverything() {
            document.getElementById('overlay').style.opacity = '0';
            setTimeout(() => { document.getElementById('overlay').style.display = 'none'; }, 500);
            
            initLyrics();
            music.play().catch(error => console.log(error));
        }

        function togglePlayPause() {
            if (music.paused) {
                music.play();
                playPauseBtn.textContent = "⏸ Pause";
            } else {
                music.pause();
                playPauseBtn.textContent = "▶ Play";
            }
        }

        music.addEventListener('timeupdate', () => {
            const currentTime = music.currentTime;
            
            const minutes = Math.floor(currentTime / 60);
            const seconds = Math.floor(currentTime % 60);
            timeViewer.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

            let activeIndex = -1;
            for (let i = 0; i < codeLines.length; i++) {
                if (currentTime >= codeLines[i].time) {
                    activeIndex = i;
                } else {
                    break;
                }
            }

            if (activeIndex !== -1 && activeIndex !== currentLineIndex) {
                currentLineIndex = activeIndex;
                triggerLineAnimation(currentLineIndex);
            }
        });

        async function triggerLineAnimation(index) {
            const lineData = codeLines[index];
            const lineElement = document.getElementById(`line-${index}`);
            
            if (!lineElement || lineElement.classList.contains('animated')) return;
            
            document.querySelectorAll('.line').forEach(el => el.classList.remove('active', 'cursor'));
            lineElement.classList.add('active', 'cursor', 'animated');
            
            const text = lineData.text;
            let currentText = "";
            const charSpeed = 35; 

            for (let char of text) {
                currentText += char;
                lineElement.textContent = currentText;
                terminal.scrollTop = terminal.scrollHeight;
                await new Promise(resolve => setTimeout(resolve, charSpeed));
            }
            
            lineElement.classList.remove('cursor');
        }
    </script>
</body>
</html>
"""

@app.route('/get_music')
def get_music():
    return send_from_directory(os.getcwd(), 'music.mp3')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
