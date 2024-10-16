<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "inscripciones_tesla";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Recibir datos del formulario
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$telefono = $_POST['telefono'];
$anio = $_POST['anio'];

// Insertar datos en la base de datos
$sql = "INSERT INTO inscripciones (nombre, email, telefono, anio) 
        VALUES ('$nombre', '$email', '$telefono', '$anio')";

if ($conn->query($sql) === TRUE) {
    echo "Inscripción exitosa";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
