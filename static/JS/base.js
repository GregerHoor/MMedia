
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

function toggleMoreOptions(element) {
    //console.log(element)
    const container = element.closest('.course-image');
    //console.log(container)
    const moreOptions = container.querySelector('.more-options');
    const arrow = element.querySelector('.arrow');

     arrow.style.transition = 'ease-in-out .1s'

    if (moreOptions.classList.contains('d-none')) {
        moreOptions.classList.remove('d-none');
        arrow.style.transform = 'rotate(90deg)';
    } else {
        moreOptions.classList.add('d-none');
        arrow.style.transform = 'rotate(0)';
    }
}