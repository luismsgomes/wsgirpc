import sys
import wsgirpc


proxy = wsgirpc.Proxy("http://localhost:5555")
for line in sys.stdin:
    print(proxy.rev(line.rstrip()))
