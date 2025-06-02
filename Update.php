<?php
// Tjek at metoden er POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo "Kun POST tilladt";
    exit;
}

// Databaseoplysninger
$host = 'localhost';
$db = 'ølbord';
$user = 'admin';
$pass = 'admin';

// Opret forbindelse
$conn = new mysqli($host, $user, $pass, $db);

// Tjek forbindelse
if ($conn->connect_error) {
    die("Forbindelse fejlede: " . $conn->connect_error);
}

// Udfør SQL-opdatering
$sql = "UPDATE drikke_logg SET liter_drukket = '0.0' WHERE id = '1'";
if ($conn->query($sql) === TRUE) {
    echo "Database opdateret!";
} else {
    echo "Fejl: " . $conn->error;
}

$conn->close();
?>
