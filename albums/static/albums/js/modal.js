function openModal(imageSrc, caption) {
    const modal = document.getElementById('photoModal');
    const modalImg = document.getElementById('modalImage');
    const modalCaption = document.getElementById('modalCaption');
    
    modal.style.display = "block";
    modalImg.src = imageSrc;
    modalCaption.innerHTML = caption;
}

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('photoModal');
    const span = document.getElementsByClassName("modal-close")[0];

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});