if (messages.length > 0) {
    const popup = document.getElementById("message-popup");
    const messageText = document.getElementById("popup-message");
    const closeButton = document.getElementById("close-popup");

    messages.forEach(msg => {
        messageText.textContent = msg.text;
        popup.classList.add(msg.tags); // Add success/error class
        popup.style.display = "block";
    });

    closeButton.addEventListener("click", () => {
        popup.style.display = "none";
        popup.className = "popup hidden"; // Reset classes
    });
}
