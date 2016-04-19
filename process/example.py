import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.python.org/doc/',
    'http://www.baidu.com'
    ]

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
help(results[0])
pool.close()
pool.join()
