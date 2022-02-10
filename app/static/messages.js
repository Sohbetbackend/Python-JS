const messages = document.getElementById('messages')
const error = document.getElementById('error')
// const height = messages.clientHeight


window.addEventListener('DOMContentLoaded', () => {
    if (messages == null) {
        // messages.clientHeight = 1;
        error.style.display = 'flex'
    }

    // if(height) {
    //     error.style.display = 'none';
    // } else {
    //     error.style.display = 'flex'
    // }
})

