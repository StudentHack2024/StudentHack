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

document.getElementById('file-upload').addEventListener('change', function() {
    document.getElementById('file-name').textContent = this.files[0].name;
});

animate();