
import { socket } from "./socket.mjs";
socket.on('connect', function () {
    socket.emit('my event', { data: "I'm connected!" });
});

function signup() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    console.log("SIGN UP")
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log(username, password)
    
    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            // login success, maybe redirect
            // alert("Login successful: " + data.message)
            window.location.href = "/player_options"
        } else {
            alert("Login failed: " + data.message);
        }
    });
    
}

function playAsGuest() {
    console.log("Playing as guest");
}

window.socket = socket;
window.login = login;
window.signup = signup;