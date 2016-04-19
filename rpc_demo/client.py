import xmlrpclib


proxy = xmlrpclib.ServerProxy('http://localhost:8000')
print "3 is even:{0}".format(proxy.is_even(3))
print "100 is even:{0}".format(proxy.is_even(100))
