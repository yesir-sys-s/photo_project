document.addEventListener('DOMContentLoaded', function() {
    const albumCards = document.querySelectorAll('.sidebar-album-item');
    const photoGrid = document.getElementById('albumPhotos');
    
    // Add debounce function
    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Function to load photos
    const loadPhotos = async (albumId) => {
        try {
            const response = await fetch(`/albums/${albumId}/photos/`);
            const data = await response.json();
            
            photoGrid.innerHTML = data.photos.map(photo => `
                <div class="photo-card">
                    <div class="card-img-container" onclick="openModal('${photo.image}', '${photo.caption}')">
                        <img src="${photo.image}" alt="${photo.caption}" class="card-img-top">
                        <div class="card-overlay">
                            <p class="caption">${photo.caption}</p>
                        </div>
                    </div>
                </div>
            `).join('');
        } catch (error) {
            console.error('Error loading photos:', error);
        }
    };

    // Debounced version of loadPhotos
    const debouncedLoadPhotos = debounce(loadPhotos, 300);

    // Add hover handlers to album cards
    albumCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // Remove active class from all cards
            albumCards.forEach(c => c.classList.remove('active'));
            // Add active class to hovered card
            card.classList.add('active');
            
            const albumId = this.dataset.albumId;
            debouncedLoadPhotos(albumId);
        });

        // Handle click events only for controls
        card.addEventListener('click', function(e) {
            if (!e.target.closest('.album-controls')) {
                e.preventDefault();
            }
        });
    });

    // Add scroll animation observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px'
    });

    // Observe all scrollable elements
    document.querySelectorAll('.scroll-fade').forEach(el => observer.observe(el));
});