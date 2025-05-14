document.addEventListener('DOMContentLoaded', function () {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function () {
            const inputId = this.getAttribute('data-input');
            const input = document.getElementById(inputId);

            const isPassword = input.type === 'password';
            input.type = isPassword ? 'text' : 'password';
            this.src = isPassword ? '/static/img/olho-aberto.png' : '/static/img/olho-fechado.png';
        });
    });
});