function likeUnlikePost(photoId) {
    const likeButton = document.getElementById(`like-button-${photoId}`);
    const likesCountSpan = document.getElementById(`likes-count-${photoId}`);

    // Provide immediate feedback by toggling the button appearance
    likeButton.classList.add('loading');
    //likeButton.classList.add('liked-animation');

    fetch(`/like-unlike-post/${photoId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // Ensure CSRF token is included
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'photo_id': photoId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        likesCountSpan.innerText = data.likes_count + ' likes';
        if (data.liked) {
            likeButton.classList.add('liked');
        } else {
            likeButton.classList.remove('liked');
        }
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
        alert('Something went wrong! Please try again.');
    })
    .finally(() => {
        likeButton.classList.remove('loading');
    });
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setupDoubleTapListener() {
    document.querySelectorAll('.post-media').forEach(media => {
      let lastTap = 0;
      media.addEventListener('click', function(e) {
        const currentTime = new Date().getTime();
        const tapLength = currentTime - lastTap;
        if (tapLength < 500 && tapLength > 0) {
          const photoId = this.getAttribute('data-photo-id');
          likeUnlikePost(photoId);
        }
        lastTap = currentTime;
      });
    });
  }
  
  document.addEventListener('DOMContentLoaded', (event) => {
    setupDoubleTapListener();
   
  });
  