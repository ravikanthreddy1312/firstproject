function loadProject(project, color) {
    fetch(`projects/${project}.html`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("content_div").style.backgroundColor = color;
            document.getElementById("content-frame").innerHTML = data;
        })
        .catch(error => {
            document.getElementById("content-frame").innerHTML = "Failed to load project.";
            console.error("Error loading project:", error);
        });
}
