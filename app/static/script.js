async function sendMessage() {
    const inputField = document.querySelector(".chat-input input");
    const message = inputField.value;
    if (!message) return;  // Evita enviar mensajes vacíos

    const response = await fetch("http://127.0.0.1:8000/api/send-message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: message }),
    });
    console.log(await response.json())
    await receiveMessage(response)
}

async function receiveMessage(response) {
    try {
        // Convertimos la respuesta a JSON
        if (response.ok) {
            const chatMessages = document.querySelector(".chat-messages");

            // Crear el elemento de mensaje de la IA
            const botMessage = document.createElement("div");
            botMessage.classList.add("message", "message-bot"); // Aplica clases CSS
            botMessage.innerHTML = `<div class="message-content">${data.result}</div>`; // Muestra el mensaje recibido

            // Agregar el mensaje al chat
            chatMessages.appendChild(botMessage);

            // Desplazar automáticamente hacia abajo para mostrar el último mensaje
            chatMessages.scrollTop = chatMessages.scrollHeight;
        } else {
            console.error("Error en la respuesta del servidor:", data);
        }
    } catch (error) {
        console.error("Error al recibir el mensaje de la IA:", error);
    }
}


function toggleHistory() {
    var history = document.querySelector('.chat-history');
    var chat = document.querySelector('.chat-container');
    var openHistory = document.querySelector('.open-history');
    if (history.classList.contains("hidden")) {
        history.classList.remove("hidden");
        chat.classList.remove("fullscreen");
        openHistory.style.display = "none";
    } else {
        history.classList.add("hidden");
        chat.classList.add("fullscreen");
        openHistory.style.display = "block";
    }
}

async function sendMessageChat() {
    const inputField = document.querySelector(".chat-input input");
    const chatMessages = document.querySelector(".chat-messages");
    const messageText = inputField.value.trim();

    if (!messageText) return;

    // Crear el mensaje del usuario
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "message-user");
    userMessage.innerHTML = `<div class="message-content">${messageText}</div>`;

    // Agregar el mensaje del usuario al chat
    chatMessages.appendChild(userMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    inputField.value = "";

    try {
        // Enviar mensaje a FastAPI
        const response = await fetch("http://127.0.0.1:8000/api/send-message", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: messageText })
        });

        if (response.ok) {
            // Esperar y mostrar la respuesta de la IA
            receiveMessage(response);
        } else {
            console.error("Error en la respuesta de FastAPI");
        }
    } catch (error) {
        console.error("Error al enviar el mensaje:", error);
    }
}


document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".chat-input button").addEventListener("click", sendMessageChat);
});

document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.querySelector("#theme-toggle");
    const chatContainer = document.querySelector(".chat-container");
    const sendButton = document.querySelector(".chat-input button"); // Botón enviar
    const inputField = document.querySelector(".chat-input input"); // Campo de entrada

    // Listener para detectar la tecla "Enter" en el campo de entrada
    inputField.addEventListener("keydown", function (event) {
        if (event.key === "Enter") { // Verifica si se presionó Enter
            event.preventDefault(); // Evita que el Enter haga un salto de línea
            sendButton.click(); // Simula un clic en el botón "Enviar"
        }
    });

    themeToggle.addEventListener("change", function () {
        if (themeToggle.checked) {
            chatContainer.style.backgroundImage = "url('static/Image/back.jpeg')";
            document.querySelectorAll(".message-user").forEach(msg => {
                msg.style.backgroundColor = "#C70039";
            });
            document.querySelector(".chat-header").style.backgroundColor = "#C70039";
            sendButton.style.backgroundColor = "#C70039";
        } else {
            chatContainer.style.backgroundImage = "none";
            document.querySelectorAll(".message-user").forEach(msg => {
                msg.style.backgroundColor = "#6a82fb";
            });
            document.querySelector(".chat-header").style.backgroundColor = "#6a82fb";
            sendButton.style.backgroundColor = "#6a82fb";
        }
    });
});