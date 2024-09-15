function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return; // Prevent empty messages

    const chatBox = document.getElementById('chat-box');
    
    // Display user message
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);
    document.getElementById('user-input').value = ""; // Clear input

    // Simulate bot response (replace with real API response)
    setTimeout(() => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        botMessage.textContent = "I'm processing your request...";
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
    }, 1000);

    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}
