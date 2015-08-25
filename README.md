# What the pic is

It is a web app can illustrate what the picture is. The recognition part using [Cloud Sight](http://cloudsightapi.com/) API service.

# Requirements

I sugguest using [virtualenv](https://github.com/pypa/virtualenv) to install the requirements.

``` bash
(env)pip install -r requirements.txt
```

## Usage

In `ws_server` directory,

``` bash
python ws_server.py
```

to start a [WebSocket](https://zh.wikipedia.org/wiki/WebSocket) server using [autobahn](http://autobahn.ws/python/index.html) at `localhost:9000`

In the root of the project,

``` shell
python manage.py runserver
```

to start a test server at `localhost:5000`

And you can open your browser to type `localhost:5000` to enter this app.