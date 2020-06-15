
document.addEventListener('DOMContentLoaded', () => {

    // Connect to web socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Submit message
    socket.on('connect', () => {
        let button = document.getElementById('send');
        button.onclick = () => {
            const message = document.getElementById('messageInput').value;
            if (message != "") {
                socket.emit('submit message', {'message': message})
            }
        };
    });

    // When a new message is announced modify html
    socket.on('announce message', data => {
        const ul = document.getElementById('chat');
        const li = document.createElement('li');
        li.style = "color: white"
        li.innerHTML = `(${data.time}) ${data.author}: ${data.message}`;
        document.getElementById('chat').appendChild(li);
    });

});

// Send message on return key
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('messageInput').onkeyup = () => {

        if (event.keyCode === 13) {
            document.getElementById('send').click()
            document.getElementById('messageInput').value = null;
        }
    };
});
