// Most of the functionality will be placed here

var canvas = document.getElementById('my-canvas')
var ctx = canvas.getContext('2d')

function draw() {
    ctx.beginPath();
    ctx.arc(50, 50, 10, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}
setInterval(draw, 10);