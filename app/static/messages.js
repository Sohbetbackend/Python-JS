const messages = document.getElementById('messages')
const error = document.getElementById('error')
const height = messages.clientHeight


window.addEventListener('DOMContentLoaded', () => {
    if(height === 0) {
        error.style.display = 'flex';
    }
})

