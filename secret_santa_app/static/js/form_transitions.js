document.addEventListener('DOMContentLoaded', function() {
    const initialButtons = document.getElementById('initial_buttons');
    const formsWrapper = document.querySelector('.forms-wrapper');
    const createForm = document.getElementById('create_room_form');
    const joinForm = document.getElementById('join_room_form');
    const backButtons = document.querySelectorAll('.back-btn');

    function showForm(formToShow) {
        initialButtons.style.opacity = '0';
        setTimeout(() => {
            initialButtons.style.display = 'none';
            formsWrapper.style.opacity = '1';
            formsWrapper.style.pointerEvents = 'auto';
            formToShow.style.display = 'block';
        }, 300);
    }

    function hideForm() {
        formsWrapper.style.opacity = '0';
        formsWrapper.style.pointerEvents = 'none';
        setTimeout(() => {
            initialButtons.style.display = 'flex';
            setTimeout(() => {
                initialButtons.style.opacity = '1';
            }, 50);
            createForm.style.display = 'none';
            joinForm.style.display = 'none';
        }, 300);
    }

    document.getElementById('show_create_form').addEventListener('click', () => {
        showForm(createForm);
    });

    document.getElementById('show_join_form').addEventListener('click', () => {
        showForm(joinForm);
    });

    backButtons.forEach(button => {
        button.addEventListener('click', hideForm);
    });

    // Initially hide both forms
    createForm.style.display = 'none';
    joinForm.style.display = 'none';
}); 