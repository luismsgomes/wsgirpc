import pickle
import queue
import requests


__version__ = "0.0.1"


class InvalidRequest(Exception):
    pass


class Server(object):
    def __init__(self, instances):
        # a queue is used to protect instances from being shared
        #  across threads
        self.instances = queue.LifoQueue()
        for instance in instances:
            self.instances.put(instance)

    def get_method_args_kwargs(self, environ):
        try:
            method, args, kwargs = pickle.load(environ["wsgi.input"])
            return method, args, kwargs
        except:  # noqa E722
            raise InvalidRequest()

    def __call__(self, environ, start_response):
        instance = self.instances.get()
        try:
            method, args, kwargs = self.get_method_args_kwargs(environ)
            result = getattr(instance, method)(*args, **kwargs)
            response_data = pickle.dumps(result)
        except BaseException as exception:
            response_data = pickle.dumps(exception)
        self.instances.put(instance)
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/octet-stream"),
                ("Content-Length", str(len(response_data))),
            ],
        )
        return iter([response_data])


class Method(object):
    def __init__(self, addr, name):
        self.addr = addr
        self.name = name

    def __call__(self, *args, **kwargs):
        response = requests.post(
            self.addr, data=pickle.dumps([self.name, args, kwargs])
        )
        return pickle.loads(response.content)


class Proxy(object):
    def __init__(self, addr):
        self._addr = addr

    def __getattr__(self, name):
        method = Method(self._addr, name)
        setattr(self, name, method)
        return method


__all__ = ["Server", "Proxy", "InvalidRequest"]
