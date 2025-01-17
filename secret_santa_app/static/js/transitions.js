document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const initialButtons = document.getElementById('initial_buttons');
    const createForm = document.getElementById('create_room_form');
    const joinForm = document.getElementById('join_room_form');
    const showCreateBtn = document.getElementById('show_create_form');
    const showJoinBtn = document.getElementById('show_join_form');
    const backButtons = document.querySelectorAll('.back-btn');

    // Check if we're on the correct page (index page)
    if (!initialButtons || !createForm || !joinForm) {
        return; // Exit if we're not on the index page
    }

    function showForm(formElement) {
        // Prepare the transition
        formElement.style.display = 'block';
        formElement.style.opacity = '0';
        formElement.style.transform = 'translateY(20px)';
        
        // Start the transition
        requestAnimationFrame(() => {
            // Fade out buttons first
            initialButtons.classList.add('hidden');
            
            // After a short delay, show the form
            setTimeout(() => {
                formElement.style.opacity = '1';
                formElement.style.transform = 'translateY(0)';
            }, 200);
        });
    }

    function hideForm(formElement) {
        // Start form fade out
        formElement.style.opacity = '0';
        formElement.style.transform = 'translateY(20px)';
        
        // Show buttons
        initialButtons.style.display = 'flex';
        
        // After form starts fading out, fade in buttons
        setTimeout(() => {
            initialButtons.classList.remove('hidden');
            
            // Clean up after transition
            setTimeout(() => {
                formElement.style.display = 'none';
            }, 300);
        }, 200);
    }

    // Show Create Room Form
    if (showCreateBtn) {
        showCreateBtn.addEventListener('click', function() {
            showForm(createForm);
        });
    }

    // Show Join Room Form
    if (showJoinBtn) {
        showJoinBtn.addEventListener('click', function() {
            showForm(joinForm);
        });
    }

    // Back Button Handler
    backButtons.forEach(button => {
        button.addEventListener('click', function() {
            const activeForm = button.closest('form');
            hideForm(activeForm);
        });
    });
}); 