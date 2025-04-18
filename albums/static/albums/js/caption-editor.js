const getCookie = name => {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
};

const initCaptionEditors = () => {
    document.querySelectorAll('.caption[contenteditable]').forEach(caption => {
        caption.addEventListener('blur', async function() {
            const photoId = this.dataset.photoId;
            const newCaption = this.textContent;
            
            try {
                const response = await fetch(`/photo/${photoId}/update-caption/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ 
                        caption: newCaption 
                    })
                });
                
                if (!response.ok) throw new Error('Update failed');
                
                const data = await response.json();
                if (data.status === 'success') {
                    this.textContent = data.caption;
                } else {
                    throw new Error('Update failed');
                }
            } catch (error) {
                console.error('Error updating caption:', error);
                this.textContent = this.getAttribute('data-original-caption');
            }
        });

        caption.addEventListener('focus', function() {
            this.setAttribute('data-original-caption', this.textContent);
        });
    });
};

document.addEventListener('DOMContentLoaded', initCaptionEditors);
