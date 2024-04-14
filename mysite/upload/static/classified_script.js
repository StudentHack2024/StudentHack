function animate() {
    requestAnimationFrame(animate);
  
    pulseBox();
  }


// Define the pulseBox function
function pulseBox() {
    console.log("pulsing")
    const box = document.getElementById('form-total');
    box.style.animation = 'pulse 2s infinite';
}

animate();