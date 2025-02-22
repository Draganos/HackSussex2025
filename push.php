<?php
$servername = "sql211.infinityfree.com";
$username = "if0_38373169";
$password = "u72RmKPyhiDm ";
$dbname = "if0_38373169_db2025";

//Connection
$conn = new mysqli($servername, $username, $password, $dbname);

//Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

?>

