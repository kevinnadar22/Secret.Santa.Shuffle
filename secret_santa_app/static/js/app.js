// Add this script to handle form visibility
document.addEventListener('DOMContentLoaded', function () {
    const initialButtons = document.getElementById('initial_buttons');
    const createForm = document.getElementById('create_room_form');
    const joinForm = document.getElementById('join_room_form');

    // Show Create Form
    document.getElementById('show_create_form').addEventListener('click', () => {
        initialButtons.classList.add('hidden');
        createForm.classList.remove('hidden');
    });

    // Show Join Form
    document.getElementById('show_join_form').addEventListener('click', () => {
        initialButtons.classList.add('hidden');
        joinForm.classList.remove('hidden');
    });

    // Back Button Functionality
    document.querySelectorAll('.back-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            createForm.classList.add('hidden');
            joinForm.classList.add('hidden');
            initialButtons.classList.remove('hidden');
        });
    });



});
