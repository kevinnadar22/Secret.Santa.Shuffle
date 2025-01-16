// Create snowflakes
function createSnowflakes() {
    const snowflakesContainer = document.getElementById('snowflakes');
    const snowflakeChars = ['❄', '❅', '❆', '✻', '✼', '❉'];
    const numberOfSnowflakes = 30;

    for (let i = 0; i < numberOfSnowflakes; i++) {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.style.left = `${Math.random() * 100}%`;
        snowflake.style.animationDuration = `${Math.random() * 3 + 2}s`;
        snowflake.style.opacity = Math.random();
        snowflake.innerHTML = snowflakeChars[Math.floor(Math.random() * snowflakeChars.length)];
        snowflakesContainer.appendChild(snowflake);
    }
}

// Function to hide loading overlay and show content
function hideLoading() {
    const loadingOverlay = document.getElementById('loading-overlay');
    const mainContent = document.getElementById('main-content');
    
    // Add loaded class to main content
    mainContent.classList.add('loaded');
    
    // Fade out loading overlay
    loadingOverlay.style.opacity = '0';
    
    // Remove loading overlay after fade
    setTimeout(() => {
        loadingOverlay.style.display = 'none';
    }, 500);
}

// Initialize loading screen
function initializeLoading() {
    // Create snowflakes when page loads
    createSnowflakes();

    // Wait for everything to load
    window.addEventListener('load', () => {
        // Add a small delay to ensure smooth transition
        setTimeout(hideLoading, 1500);
    });

    // Fallback: Hide loading if it takes too long
    setTimeout(hideLoading, 5000);
}

// Run initialization
document.addEventListener('DOMContentLoaded', initializeLoading); 