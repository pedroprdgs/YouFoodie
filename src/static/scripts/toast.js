document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".toast").forEach(toastEl => {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000
        });
        toast.show();
    });
});