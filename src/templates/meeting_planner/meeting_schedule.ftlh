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
    <link href="<@spring.url '/css/meeting.css'/>" rel="stylesheet">

    <title>${meeting.name}</title>
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
        <div class="chat">

            <a href="#popup__chat" id="open-chat">Открыть чат</a>
            <div id="popup__chat" class="chat__field">
                <a href="#header" class="exit">×</a>
                <div class="messages" id="messages">
                    <#list messages as message>
                        <div class="message">
                            <span>${message.name} (${message.time?string} ${message.date?string})</span>
                            <span>- ${message.body?string}</span>
                        </div>
                    </#list>
                </div>
                <#if (messages?size = 0)>
                    <div style="margin-bottom: 20px"></div>
                </#if>
                <form id="message-form" class="send__message">
                    <input type="text" name="body" id="body" placeholder="Введите сообщение"/>
                    <button id="message-button" type="button">></button>
                </form>
            </div>

        </div>
        <div class="schedule__btn">
            <#if isAdmin>
                <form method="post"
                      action="<@spring.url '/meetings/${meeting.id}/sendEmail'/>">
                    <button type="submit">Разослать расписание</button>
                </form>
            </#if>
            <a class="show__schedule" role="button" href="<@spring.url '/meetings/${meeting.id}/'/>">Редактировать
                расписание</a>
        </div>
    </div>

    <div class="schedule">
        <#list weekdays as weekday>

            <#if timelinesMap[weekday.name]?size == 0>
                <div class="weekday">

            <#else>
                <div class="weekday" style="background-color: rgba(105, 219, 170, 0.8)">
            </#if>

            <h3>${weekday.name}</h3>
            <#if timelinesMap[weekday.name]??>
                <#if timelinesMap[weekday.name]?size == 0>
                    <div class="schedule__line__field">
                        <span>Встречи нет</span>
                    </div>
                </#if>

                <#list timelinesMap[weekday.name] as start, end>
                    <div class="schedule__line__field">
                        <span>${start?remove_ending(":00")} - ${end?remove_ending(":00")}</span>
                    </div>
                </#list>
            </#if>
            </div>
        </#list>
    </div>
</main>

<script src="https://cdn.jsdelivr.net/npm/sockjs-client@1/dist/sockjs.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@stomp/stompjs@6.0.0/bundles/stomp.umd.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="<@spring.url '/js/meeting.js'/>"></script>
</body>
</html>



