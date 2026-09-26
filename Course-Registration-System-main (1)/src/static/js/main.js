document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("form[action*=cancel]").forEach((form) => {
        form.addEventListener("submit", (event) => {
            if (!window.confirm("Bạn chắc chắn muốn hủy đăng ký lớp này?")) {
                event.preventDefault();
            }
        });
    });
});
