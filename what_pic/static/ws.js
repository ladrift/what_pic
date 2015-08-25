var socket = null;
var isopen = false;

window.onload = function() {

    socket = new WebSocket("ws://127.0.0.1:9090");
    socket.binaryType = "arraybuffer";

    socket.onopen = function() {
        console.log("Connected!");
        isopen = true;
    };

    socket.onmessage = function(e) {
        if (typeof e.data == "string") {
            console.log("Text message received: " + e.data);

            var msg = JSON.parse(e.data);
            var output = document.getElementById("result");
            switch (msg.title) {
                case "response":
                    if (msg.content == "uploaded") {
                        // change output to 'processing...'
                        output.innerHTML = "processing...";
                    } else if (msg.content == "mistake") {
                        // change to mistake notice
                        output.innerHTML = "mistake happened.";
                    }
                    break;
                case "result":
                    // change to value of `msg.content`
                    output.innerHTML = msg.content
                    break;
            }
            
        } else {
            var arr = new Uint8Array(e.data);
            var hex = '';
            for (var i = 0; i < arr.length; i++) {
                hex += ('00' + arr[i].toString(16)).substr(-2);
            }
            console.log("Binary message received: " + hex);
        }
    }

    socket.onclose = function(e) {
        console.log("Connection closed.");
        socket = null;
        isopen = false;
    }
};

function sendURL(url) {
    var msg = {
        title: "URL",
        content: url
    };

    socket.send(JSON.stringify(msg));
    document.getElementById("url").value = "";
};

function sendText() {
    if (isopen) {
        socket.send("Hello, world!");
        console.log("Text message sent.");               
    } else {
        console.log("Connection not opened.")
    }
};

function sendBinary() {
    if (isopen) {
        var buf = new ArrayBuffer(32);
        var arr = new Uint8Array(buf);
        for (i = 0; i < arr.length; ++i) arr[i] = i;
        socket.send(buf);
        console.log("Binary message sent.");
    } else {
        console.log("Connection not opened.")
    }
};
