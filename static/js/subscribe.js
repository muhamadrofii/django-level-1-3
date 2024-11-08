// subscribe.js

document.addEventListener("DOMContentLoaded", function() {
    // Check if the success message exists
    const successMessage = document.getElementById('successMessage');
    if (successMessage) {
        successMessage.style.display = 'block'; // Show message

        // Hide the success message after 3 seconds
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
    }
});
