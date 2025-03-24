document.addEventListener("DOMContentLoaded", function () {
    fetch("index.JSON")
        .then(response => response.json())
        .then(tasks => {
            const taskList = document.getElementById("task-list");
            const contentFrame = document.getElementById("content-frame");

            tasks.forEach(task => {
                let listItem = document.createElement("li");
                listItem.textContent = task.title;
                listItem.classList.add("task-item");

                listItem.addEventListener("click", () => {
                    contentFrame.src = task.file;
                });

                taskList.appendChild(listItem);
            });
        })
        .catch(error => console.error("Error loading tasks:", error));
});
