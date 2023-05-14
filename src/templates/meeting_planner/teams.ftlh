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
    <link href="<@spring.url '/css/teams.css'/>" rel="stylesheet">

    <title>Команды</title>
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
    <div class="main__top">
        <div class="add__team">
            <a href="#popup">Добавить команду</a>
        </div>
        <h3>Команды</h3>
        <form class="search">
            <input placeholder="Название команды" type="search" aria-label="Поиск">
            <button type="submit">Поиск</button>
        </form>
    </div>

    <div id="popup" class="popup__add__team">
        <div class="popup__add__team__window">
            <a href="#header" class="exit">×</a>
            <h3>Добавить команду</h3>
            <div class="add__team__blocks">
                <form class="add__team__block" method="post" action="<@spring.url '/teams/enter'/>">
                    <input placeholder="Название" name="name" type="text">
                    <input placeholder="Пароль" name="password" type="password">
                    <button type="submit">Войти</button>
                </form>
                <form class="add__team__block" method="post" action="<@spring.url '/teams/create'/>">
                    <input placeholder="Название" name="name" type="text">
                    <input placeholder="Пароль" name="password" type="password">
                    <button type="submit">Создать</button>
                </form>
            </div>
        </div>
    </div>

    <div class="teams">
        <#list teams as team>
            <div class="team">
                <div>
                    <div class="team__inf">
                        <h3>${team.name}</h3>
                        <span>Админ: ${team.adminName}</span>
                        <span>Пароль: ${team.password}</span>
                    </div>

                    <form class="rename" method="post" action="<@spring.url '/teams/changeTeamName'/>">
                        <label>
                            <input type="hidden" name="id" value="${team.id}">
                            <input type="text" name="name" placeholder="Переименовать">
                        </label>
                        <button type="submit">✓</button>
                    </form>
                </div>

                <div class="team__btn">
                    <a role="button" class="enter" href="<@spring.url '/teams/${team.id}'/>">Перейти</a>
                    <#if team.adminId != currentUserId>
                        <form method="post" action="<@spring.url '/teams/leave/${team.id}'/>">
                            <button type="submit" class="leave">Выйти</button>
                        </form>
                    <#else>
                        <form method="post" action="<@spring.url '/teams/delete/${team.id}'/>">
                            <button type="submit" class="leave">Удалить</button>
                        </form>
                    </#if>
                </div>
            </div>
        </#list>
    </div>
</main>


</body>
</html>