function openModal(imageSrc, caption) {
    const modal = document.getElementById('photoModal');
    const modalImg = document.getElementById('modalImage');
    const modalCaption = document.getElementById('modalCaption');
    
    modal.style.display = "flex";
    modal.style.alignItems = "center";
    modal.style.justifyContent = "center";
    
    modalImg.src = imageSrc;
    modalCaption.innerHTML = caption;

    // Center image and handle window resize
    const centerImage = () => {
        const vhHeight = window.innerHeight * 0.8; // Changed from 0.95
        const vwWidth = window.innerWidth * 0.8;   // Changed from 0.95
        modalImg.style.maxHeight = `${vhHeight}px`;
        modalImg.style.maxWidth = `${vwWidth}px`;
    };

    centerImage();
    window.addEventListener('resize', centerImage);
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