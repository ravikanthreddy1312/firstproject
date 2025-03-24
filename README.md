<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Gallery</title>
    <link rel="stylesheet" href="index.css">
    <script>
        
    body {
    font-family: Arial, sans-serif;
    display: flex;
    margin: 0;
    height: 100vh;
    }
    
    .container {
    display: flex;
    width: 100%;
    }
    
    .sidebar {
    width: 25%;
    background: #333;
    color: white;
    padding: 15px;
    height: 100vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    }
    
    .sidebar h2 {
    text-align: center;
    }
    
    ul {
    list-style: none;
    padding: 0;
    margin: 0;
    flex-grow: 1;
    }
    
    .task-item {
    padding: 10px;
    cursor: pointer;
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    width: 100%;
    }
    
    .task-item:hover {
    background: #555;
    }
    
    .content {
    width: 75%;
    padding: 20px;
    }
    
    iframe {
    width: 100%;
    height: 100%;
    border: none;
    }
    
    </script>
</head>
<body>
    <div class="container">
        <nav class="sidebar">
            <h2>Class Works</h2>
            <ul id="task-list"></ul>
        </nav>
        <main class="content">
            <iframe id="content-frame" src="" frameborder="0"></iframe>
        </main>
    </div>

    <script src="index.js"></script>
</body>
</html>
