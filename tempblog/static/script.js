document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll('.form__btn_delete');
    const confirmationCards = document.querySelectorAll('.confirmation-card');

    deleteButtons.forEach((deleteButton, index) => {
        deleteButton.onclick = function () {
            console.log("Delete button clicked");
            confirmationCards[index].style.display = 'block';
        };
    });
});

