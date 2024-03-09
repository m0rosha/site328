document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartLink = document.querySelector('.cart_word');

    let cartItems = [];

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.getAttribute('data-product-id');
            const productName = this.getAttribute('data-product-name');
            const productPrice = this.getAttribute('data-product-price');

            const newItem = {
                id: productId,
                name: productName,
                price: productPrice
            };

            cartItems.push(newItem);
            updateCartLink();

            
        });
    });

    function updateCartLink() {
        cartLink.textContent = `Your Cart (${cartItems.length} items)`;
    }
});