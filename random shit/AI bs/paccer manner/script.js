const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let pacManX = 50;
let pacManY = 50;

function drawPacMan() {
  ctx.beginPath();
  ctx.arc(pacManX, pacManY, 15, 0.2 * Math.PI, 1.8 * Math.PI);
  ctx.lineTo(pacManX, pacManY);
  ctx.fillStyle = 'yellow';
  ctx.fill();
  ctx.closePath();
}

function gameLoop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawPacMan();
  // Other game logic and rendering code here
  requestAnimationFrame(gameLoop);
}

gameLoop();