document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");

    function appendMessage(message, sender) {
        const msgDiv = document.createElement("div");
        msgDiv.classList.add("message", sender);
        msgDiv.textContent = message;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        appendMessage(text, "user");
        userInput.value = "";

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            if (data.bot_response) {
                appendMessage(data.bot_response, "bot");
            } else {
                appendMessage("Something went wrong!", "bot");
            }
        } catch (error) {
            appendMessage("Error connecting to server!", "bot");
        }
    }

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });
});
