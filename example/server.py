import wsgirpc


class Reverser(object):
    def rev(self, line):
        return line[::-1]


app = wsgirpc.Server([Reverser()])


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 5555, app) as httpd:
        print("Serving on port 5555...")
        httpd.serve_forever()
