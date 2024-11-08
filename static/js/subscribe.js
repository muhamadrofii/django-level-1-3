// subscribe.js
document.addEventListener("DOMContentLoaded", function() {

    const successMessage = document.getElementById('successMessage');
    if (successMessage) {
        successMessage.style.display = 'block'; 

        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
    }
});
