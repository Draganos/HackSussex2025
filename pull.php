<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
ob_clean();  // Prevent InfinityFree from adding extra output
error_reporting(0); // Disable error messages (prevents HTML noise)

$servername = "sql211.infinityfree.com";
$username = "if0_38373169";
$password = "u72RmKPyhiDm";
$dbname = "if0_38373169_db2025";

// Establish connection
$db = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($db->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $db->connect_error]));
}

// Validate input
$PersonID = isset($_POST['PersonID']) ? intval($_POST['PersonID']) : 0;
if ($PersonID == 0) {
    die(json_encode(["error" => "Invalid Person ID"]));
}

// Query database
$result = $db->query("SELECT * FROM DatabaseA WHERE PersonID = $PersonID");

if ($result && $row = $result->fetch_assoc()) {
    echo json_encode($row);
} else {
    echo json_encode(["error" => "No data found"]);
}

$db->close();
exit();
?>
