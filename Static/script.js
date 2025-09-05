// static/script.js

document.addEventListener("DOMContentLoaded", () => {
    const socket = io();
    const form = document.getElementById("chat-form");
    const input = document.getElementById("message");
    const messages = document.getElementById("messages");

    // Incoming message
    socket.on("message", (msg) => {
        const li = document.createElement("li");
        li.textContent = msg;
        li.classList.add("incoming");
        messages.appendChild(li);
        messages.scrollTop = messages.scrollHeight; // auto scroll
    });

    // Outgoing message
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        if (input.value.trim()) {
            const msg = input.value;
            socket.send(msg);

            // Show outgoing message instantly
            const li = document.createElement("li");
            li.textContent = msg;
            li.classList.add("outgoing");
            messages.appendChild(li);
            messages.scrollTop = messages.scrollHeight;

            input.value = "";
        }
    });
});
