<!DOCTYPE html>
<html>
<head>
  <title>Результат входа</title>
</head>
<body>

<?php if (isset($error_message)) { ?>
  <p><?php echo $error_message; ?></p>
<?php } else { ?>
  <p>Добро пожаловать, <?php echo $username; ?>!</p>
<?php } ?>

</body>
</html>