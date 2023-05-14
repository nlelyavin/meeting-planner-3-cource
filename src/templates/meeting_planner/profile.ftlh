<#ftl encoding='utf-8'>
<#import '/spring.ftl' as spring>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

    <link href="<@spring.url '/css/zeroing_styles.css'/>" rel="stylesheet">
    <link href="<@spring.url '/css/header_style.css'/>" rel="stylesheet">
    <link href="<@spring.url '/css/profile.css'/>" rel="stylesheet">

    <title>Профиль</title>
</head>
<body>

<header class="header" id="header">
    <a href="<@spring.url '/' />" class="logo">Meeting Planner</a>
    <nav class="nav">
        <a href="<@spring.url '/teams' />">Мои команды</a>
        <a href="<@spring.url '/profile' />">Профиль</a>
    </nav>
</header>

<main class="main">
    <div class="profile__card">
        <div class="profile__nick">
            <span>${user.getUserNickname()}</span>
        </div>
        <div class="profile__img">
            <img src="<@spring.url '/img/ava.png'/>" alt="">
        </div>
        <div class="profile__name">
            <span>${user.getName()}</span>
        </div>
        <div class="profile__email">
            <span>${user.getUsername()}</span>
        </div>
        <form action="/logout" target="_blank">
            <button>Выйти</button>
        </form>
    </div>
</main>

<footer class="footer">

</footer>

</body>
</html>
