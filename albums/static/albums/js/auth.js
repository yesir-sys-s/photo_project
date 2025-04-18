document.addEventListener('DOMContentLoaded', function() {
    const flipTriggers = document.querySelectorAll('.flip-trigger');
    const authCard = document.querySelector('.auth-card');
    const loadingOverlay = document.querySelector('.loading-overlay');

    flipTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            const targetUrl = this.getAttribute('href');
            
            authCard.classList.add('flipped');
            setTimeout(() => {
                loadingOverlay.classList.remove('d-none');
            }, 300);
            
            setTimeout(() => {
                window.location.href = targetUrl;
            }, 600);
        });
    });

    // Add click handlers to password toggle icons
    document.querySelectorAll('.input-group-text .bi').forEach(icon => {
        icon.addEventListener('click', togglePassword);
    });
});

function togglePassword(button) {
    const passwordField = button.parentElement.querySelector('input');
    const icon = button.querySelector('i');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        passwordField.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
}