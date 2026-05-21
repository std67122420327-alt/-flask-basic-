<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Music Player Player</title>
</head>
<body>
    <audio id="player" loop>
        <source src="music.mp3" type="audio/mpeg">
    </audio>

    <script>
        // ฟังก์ชันสั่งให้เพลงเล่น (จะถูกเรียกจากไฟล์ index.html)
        function playSong() {
            const audio = document.getElementById('player');
            audio.play().catch(err => console.log("Playback blocked:", err));
        }
        
        // ฟังก์ชันสั่งให้เพลงหยุด
        function stopSong() {
            const audio = document.getElementById('player');
            audio.pause();
        }
    </script>
</body>
</html>
