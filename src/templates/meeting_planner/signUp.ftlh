<#ftl encoding='utf-8'>
<#import '/spring.ftl' as spring>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

    <link href="<@spring.url '/css/zeroing_styles.css'/>" rel="stylesheet">
    <link href="<@spring.url '/css/header_style.css'/>" rel="stylesheet">
    <link href="<@spring.url '/css/sign_in.css'/>" rel="stylesheet">

    <title>Регистрация</title>
</head>
<body>

<header class="header" id="header">
    <a href="<@spring.url '/' />" class="logo">Meeting Planner</a>
</header>

<main class="main">
    <form action="/signUp" method="post" class="sign__in__card">
        <h3>Регистрация</h3>

        <input type="text" placeholder="Имя" name="firstName">
        <input type="text" placeholder="Фамилия" name="lastName">
        <input type="text" placeholder="Имя пользователя" name="userName">
        <input type="email" placeholder="Почта" name="email">
        <input type="password" placeholder="Пароль" name="password">

        <div class="sign__in__btn">
            <div class="sign__up__btn">
                <button type="submit">Регистрация</button>
            </div>
        </div>
    </form>
    </div>
</main>


<footer class="footer">

</footer>


</body>
</html>