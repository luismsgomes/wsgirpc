import wsgirpc


class Reverser(object):
    def rev(self, line):
        return line[::-1]

    def exc(self, depth):
        if depth <= 0:
            raise Exception("this is an example exception")
        else:
            self.exc(depth-1)


app = wsgirpc.Server([Reverser()])


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 5555, app) as httpd:
        print("Serving on port 5555...")
        httpd.serve_forever()
