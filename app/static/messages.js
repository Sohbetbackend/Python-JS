const messages = document.getElementById('messages')
const error = document.getElementById('error')

window.addEventListener('DOMContentLoaded', () => {
    if(messages.style.height <= 1) {
        error.style.display = 'flex';
    }
})

