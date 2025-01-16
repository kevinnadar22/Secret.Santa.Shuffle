function createSnowfall() {
    const snowContainer = document.createElement('div');
    snowContainer.style.position = 'fixed';
    snowContainer.style.top = '0';
    snowContainer.style.left = '0';
    snowContainer.style.width = '100%';
    snowContainer.style.height = '100%';
    snowContainer.style.pointerEvents = 'none';
    snowContainer.style.zIndex = '1';
    document.body.appendChild(snowContainer);

    function createSnowflake() {
        const snowflake = document.createElement('div');
        snowflake.className = 'snow-particle';
        
        // Random properties
        const size = Math.random() * 5 + 2;
        const startingLeft = Math.random() * 100;
        const animationDuration = Math.random() * 3 + 2;
        const opacity = Math.random() * 0.6 + 0.4;
        
        snowflake.style.width = `${size}px`;
        snowflake.style.height = `${size}px`;
        snowflake.style.left = `${startingLeft}%`;
        snowflake.style.animationDuration = `${animationDuration}s`;
        snowflake.style.opacity = opacity;
        
        snowContainer.appendChild(snowflake);
        
        // Remove snowflake after animation
        setTimeout(() => {
            snowflake.remove();
        }, animationDuration * 1000);
    }

    // Create snowflakes periodically
    setInterval(createSnowflake, 100);
}

document.addEventListener('DOMContentLoaded', createSnowfall); 