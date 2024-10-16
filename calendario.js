function showModal(event) {
    const modal = document.getElementById("modal");
    const modalText = document.getElementById("modal-text");

    modalText.innerText = information[event] || "Información no disponible.";
    modal.style.display = "block";
}

function showModal(eventTitle) {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');

    modalTitle.textContent = eventTitle;
    modalDescription.textContent = `${eventTitle}.`;
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
}

// Close modal when clicking outside of the modal content
window.onclick = function(event) {
    const modal = document.getElementById("modal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
