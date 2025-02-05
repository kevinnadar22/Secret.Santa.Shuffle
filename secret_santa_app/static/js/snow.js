function createSnowfall() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    // Set canvas to full screen
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '1';
    
    // Set actual canvas dimensions
    function setCanvasSize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    setCanvasSize();
    window.addEventListener('resize', setCanvasSize);
    
    document.body.appendChild(canvas);
    
    // Snowflake particles
    const maxParticles = 100; // Limit total particles
    const particles = [];
    
    class Particle {
        constructor() {
            this.reset();
        }
        
        reset() {
            this.x = Math.random() * canvas.width;
            this.y = 0;
            this.size = Math.random() * 3 + 2;
            this.speed = Math.random() * 1 + 0.5;
            this.opacity = Math.random() * 0.6 + 0.4;
            this.wind = Math.random() * 0.5 - 0.25;
        }
        
        update() {
            this.y += this.speed;
            this.x += this.wind;
            
            // Reset particle when it goes off screen
            if (this.y > canvas.height) {
                this.reset();
            }
            if (this.x > canvas.width) {
                this.x = 0;
            } else if (this.x < 0) {
                this.x = canvas.width;
            }
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.fill();
        }
    }
    
    // Initialize particles
    for (let i = 0; i < maxParticles; i++) {
        particles.push(new Particle());
    }
    
    // Animation loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
}

document.addEventListener('DOMContentLoaded', createSnowfall); 