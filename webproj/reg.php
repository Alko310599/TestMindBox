<?php

// Проверяем, была ли отправлена форма методом POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    // Получаем данные из формы
    $username = $_POST['username'];
    $password = $_POST['password'];
    $login = $_POST['login'];
    $email = $_POST['email'];

    // Подключаемся к базе данных SQLite
    $db = new SQLite3('path/to/database.db');

    // Проверяем, что соединение с базой данных установлено успешно
    if (!$db) {
        die('Could not connect to database.');
    }

    // Выполняем запрос на добавление данных в таблицу users
    $query = "INSERT INTO users (username, login, email, password) VALUES ('$username', '$login', '$email', '$password')";
    $result = $db->exec($query);

    // Проверяем, что запрос выполнен успешно
    if ($result) {
        echo "Data added to database.";
    } else {
        echo "Error adding data to database.";
    }

    // Закрываем соединение с базой данных
    $db->close();
}
?>