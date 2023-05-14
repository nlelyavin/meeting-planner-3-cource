let stompClient = null;

function connect() {
    let socket = new SockJS('/websocket');
    stompClient = StompJs.Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        console.log('Connected :' + frame);
        stompClient.subscribe(window.location.pathname, function (dto) {
            let message = JSON.parse(dto.body);
            showMessage(message.name, message.time, message.date, message.body);
            setScrollIntoView(false);
        });
    });
}

function sendMessage() {
    let meetingId = window.location.pathname.slice(-1);
    let url = '/chat/' + meetingId;
    stompClient.send(url, {}, JSON.stringify({
        'body': $('#body').val()
    }));
    $('#body').val('');
}

function showMessage(name, time, date, body) {
    $('#messages').append(
        '<div class="message">' +
            '<span>' + name + ' (' + time + ' ' + date + ')' + '</span>' +
            '<span>' + '- ' + body + '</span>' +
        '</div>'
    );
}

function setScrollIntoView(top) {
    const message = document.querySelectorAll('.message');
    const lastMessage = message[message.length - 1];
    const lastMessageTexts = lastMessage.querySelectorAll('span');
    const lastMessageText = lastMessageTexts[lastMessageTexts.length - 1];
    lastMessageText.scrollIntoView(top);
}

$(function () {
    $('#open-chat').click(function (ev) {
        setScrollIntoView(false);
    });

    $('#message-form').submit(function (ev) {
        ev.preventDefault();
    });
    connect();
    $('#message-button').click(function (ev) {
        sendMessage();
        setScrollIntoView(false);
    });

    $("button.delete__timeline").click(function (ev) {
        let weekday = $(this).attr("data-weekday");
        let startTime = $(this).attr("data-start-time");
        let endTime = $(this).attr("data-end-time");
        let ajaxUrl = window.location.pathname + "/schedule/delete";
        console.log("You pressed the button");
        $.ajax({
            url: ajaxUrl,
            method: 'POST',
            data: {
                'weekdayName': weekday,
                'startTime': startTime,
                'endTime': endTime
            },
            success: function (data) {
                window.location.reload();
            },
            error: function () {
                console.log("Something went wrong");
            }
        });
    });
});