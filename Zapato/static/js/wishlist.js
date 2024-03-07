// static/js/wishlist.js
document.addEventListener('DOMContentLoaded', function () {
    const wishlistButtons = document.querySelectorAll('.wishlist-button');

    wishlistButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the anchor tag from navigating

            const itemId = this.getAttribute('data-item-id');

            fetch(`/toggle-wishlist/${itemId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        this.style.backgroundColor = data.added_to_wishlist ? 'red' : '';
                        this.textContent = data.added_to_wishlist ? 'Remove from Wishlist' : 'Add to Wishlist';
                    }
                });
        });
    });
});
