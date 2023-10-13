<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $username = $_POST['username'];
  $password = $_POST['password'];

  $db = new SQLite3('mydatabase.db');

  // проверка логина и пароля
  $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";

// выполняем запрос и получаем результат
$result = $db->query($query);

// проверяем, есть ли запись с заданным логином и паролем
if ($result->fetchArray()) {
  header('Location: mySite.html');
  exit;
} else {
 // если логин или пароль неправильные, показать сообщение об ошибке
 header('Location: mySite.html');
 $error_message = 'Неправильный логин или пароль. Попробуйте еще раз.';
}
 
}
?>

