document.querySelectorAll(".faq-question").forEach(button => {
    button.addEventListener("click", () => {
        const item = button.parentElement;
        item.classList.toggle("open");
    });
});

function searchHelp() {
    const query = document.getElementById("helpSearch")
        .value.toLowerCase().trim();

    document.querySelectorAll(".faq-item").forEach(item => {
        item.style.display =
            item.innerText.toLowerCase().includes(query) ? "" : "none";
    });
}