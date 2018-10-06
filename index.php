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
        $parts = explode("£££", $tweet, 3);
        $parts[1] = "@".$parts[1];
        echo "<div class='container'><span class='box'><li class='comment-body'><img src='".$parts[0]."' width=48 height = 48><h5 class='username'>".$parts[1]."</h5>"."<p>".$parts[3]."</p>"."</li></span></div>";
    }
    fclose($pythonoutput);
    ?>
    </ul>
</body>
</html>
