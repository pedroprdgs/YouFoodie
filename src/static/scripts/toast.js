document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".toast").forEach(toastEl => {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000
        });
        toast.show();
    });
});

function showToast(message, type="success"){
    let container = document.querySelector(".toast-container");

    if(!container){
        container = document.createElement("div");
        container.className = "toast-container position-fixed top-0 end-0 p-3";
        container.computedStyleMap.zIndex = "9999";
        document.body.appendChild(container);
    }

    const toastEl = document.createElement("div");
    toastEl.className = `toast align-items-center text-bg-${type} border-0`;

    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button
                type="button"
                class="btn-close btn-close-white me-2 m-auto"
                data-bs-dismiss="toast">
            </button>
        </div>
    `;

    container.appendChild(toastEl);

    const toast = new bootstrap.Toast(toastEl, {
        delay: 3000
    });

    toast.show();

    toastEl.addEventListener("hidden.bs.toast", () => {
        toastEl.remove();
    });
}