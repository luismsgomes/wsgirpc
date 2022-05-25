import wsgirpc


proxy = wsgirpc.Proxy("http://localhost:5555")

# this should raise an exception:
proxy.exc(3)
