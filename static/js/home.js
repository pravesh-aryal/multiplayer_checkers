var socket = io();

socket.on('connect', function () {
    socket.emit('my event', { data: "I'm connected!" });
});

function signup() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log("Signup clicked:", username, password);
    // socket.emit(...) or fetch(...)
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        console.log('Response from server:', data);
    });
}

function playAsGuest() {
    console.log("Playing as guest");
}
