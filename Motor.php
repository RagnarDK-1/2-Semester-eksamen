<?php
// Vis fejl (kun til test)
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Database detaljer
$servername = "localhost"; 
$username = "admin";       
$password = "admin";       
$db = "motor";

// Opret forbindelse
$conn = new mysqli($servername, $username, $password, $db);

// Tjek forbindelsen
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Hent den aktuelle værdi for ID=1
$sql_select = "SELECT status FROM motor_kontrol WHERE id = 1";
$result = $conn->query($sql_select);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $currentValue = (int)$row['status'];
    echo "Nuværende værdi: $currentValue<br>";

    // Skift 1 til 0 eller 0 til 1
    $newValue = $currentValue === 1 ? 0 : 1;

    $sql_update = "UPDATE motor_kontrol SET status = $newValue WHERE id = 1";

    if ($conn->query($sql_update) === TRUE) {
        echo "Værdi opdateret til: $newValue";
    } else {
        echo "Fejl ved opdatering: " . $conn->error;
    }
} else {
    echo "Ingen data fundet med id=1";
}

$conn->close();
?>
