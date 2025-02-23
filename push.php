<?php
$servername = "sql211.infinityfree.com";
$username = "if0_38373169";
$password = "u72RmKPyhiDm ";
$dbname = "if0_38373169_db2025";

//connection
$db = new mysqli($servername, $username, $password, $dbname);

//Check connection
if ($db->dbect_error) {
  die("connection failed: " . $db->dbect_error);
}
echo "connected successfully";

$person_id = $_POST['PersonID'] ?? null;
$driver_score = $_POST['DriverScore'] ?? null;

if ($person_id === null || $driver_score === null) {
    die("Error: Missing required fields.");
}

// Sanitize input
$person_id = $db->real_escape_string($person_id);
$driver_score = floatval($driver_score);

// Insert or update the database
$sql = "INSERT INTO driver_scores (PersonID, DriverScore) 
        VALUES ('$person_id', '$driver_score') 
        ON DUPLICATE KEY UPDATE DriverScore = '$driver_score'";

if ($db->query($sql) === TRUE) {
    echo "Data successfully stored.";
} else {
    echo "Error: " . $db->error;
}

// Close dbection
$db->close();
?>

