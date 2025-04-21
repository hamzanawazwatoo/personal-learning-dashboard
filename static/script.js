// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // Form validation for Add Goal
    const goalForm = document.querySelector("form[action='/add_goal']");
    if (goalForm) {
        goalForm.addEventListener("submit", (e) => {
            const title = goalForm.querySelector("input[name='title']").value.trim();
            const deadline = goalForm.querySelector("input[name='deadline']").value;

            if (!title || !deadline) {
                alert("Please fill out both fields before submitting.");
                e.preventDefault(); // Prevent form from submitting
            }
        });
    }

    // Confirmation before marking goal as complete (if implemented)
    const completeButtons = document.querySelectorAll(".complete-button");
    completeButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const confirmed = confirm("Are you sure you want to mark this goal as complete?");
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });

    // Highlight deadlines that are approaching
    const rows = document.querySelectorAll("table tr");
    const today = new Date();

    rows.forEach(row => {
        const deadlineCell = row.querySelector("td:nth-child(2)");
        if (deadlineCell) {
            const deadlineDate = new Date(deadlineCell.textContent);
            const diffDays = (deadlineDate - today) / (1000 * 60 * 60 * 24);

            if (diffDays >= 0 && diffDays <= 3) {
                deadlineCell.style.color = "orange";
                deadlineCell.style.fontWeight = "bold";
            } else if (diffDays < 0) {
                deadlineCell.style.color = "red";
            }
        }
    });

});
