# WSGI-based RPC

Why this package?

1. JSON-RPC is easy and fast, but you need to convert your arguments and return values to basic python types (strings, lists, dicts, etc)
1. Pyro and RPyC are very powerful, but sometimes you don't need nor want every object to be proxied over sockets.

This package provides the ability to invoque methods on a remote object with pickable arguments and receiving a pickable object on return.

All objects are passed into and from the remote method by value.


# Running the included example

To run the example server with Python's wsgi reference implemetantion:

    $ python example/server.py


To run the example server with gunicorn:

    $ cd example && gunicorn -b localhost:5555 server:app


To run the client:

    
    $ echo Hello world | python example/client.py
    dlrow olleH