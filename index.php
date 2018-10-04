<!doctype html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
    <link rel="stylesheet" href="app.css">
    <title>Twitter Bot</title>
</head>
<body>
    <ul id="tweets">
    <?php
    $pythonoutput = fopen("output.txt", "r") or die("Unable to open file");
    while (!feof($pythonoutput)) {
        $tweet = fgets($pythonoutput);
        $parts = explode(":", $tweet, 2);
        $userName = explode("@", $parts[0], 2);
        $parts[0] = "@".$userName[1];
        echo "<div class='container'><span class='box'><li class='comment-body'><h5 class='username'>".$parts[0]."</h5>"."<p>".$parts[1]."</p>"."</li></span></div>";
    }
    fclose($pythonoutput);
    ?>
    </ul>
</body>
</html>
