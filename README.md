# WSGI-based RPC

Why this package?

1. JSON-RPC is easy and fast, but you need to convert your arguments and return values to basic python types (strings, lists, dicts, etc)
1. Pyro and RPyC are very powerful, but sometimes you don't need nor want every object to be proxied over sockets.

This package provides the ability to invoque methods on a remote object with pickable arguments and receiving a pickable object on return.

This module is about 70 lines of code and depends only on Python and `requests` package.

This implementation is supposed to be fast while being easy to understand.


# Running the included example

The included example implements a program that mimics the Linux `rev` command.
The client program runs a loop that reads a line of text from stdin, sends it to
the server which reverses it and returns it back to the client, which prints it to stdout.


To run the example server with Python's wsgi reference implemetantion:

    $ python example/server.py


To run the example server with gunicorn:

    $ cd example && gunicorn -b localhost:5555 server:app


To run the client:

    $ echo Hello world | python example/client.py
    dlrow olleH


# License

This Python module is licensed under the MIT license.


