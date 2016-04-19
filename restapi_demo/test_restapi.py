import base64
import httplib2
from urllib import urlencode
import json
import pprint


def get_all():
    h = httplib2.Http()
    resp, content = h.request(
        'http://127.0.0.1:8000/snippets/',
        'GET',
    )
    pprint.pprint(json.loads(content))

def get():
    h = httplib2.Http()
    resp, content = h.request(
        'http://127.0.0.1:8000/snippets/3/',
        'GET',
    )
    pprint.pprint(json.loads(content))



def post():
    #httplib2.debuglevel = 1
    h = httplib2.Http()
    data = dict(code="print 'asd asd'")
    auth = base64.encodestring( 'iye' + ':' + 'asdasd' )
    resp, content = h.request(
        'http://127.0.0.1:8000/snippets/',
        'POST',
        json.dumps(data),
        headers = { 'Authorization' : 'Basic ' + auth ,'Content-Type': 'application/json; charset=UTF-8'}
    )
    print content

def delete():
    h = httplib2.Http()
    auth = base64.encodestring( 'iye' + ':' + 'asdasd' )
    resp, content = h.request(
        'http://127.0.0.1:8000/snippets/2/',
        'DELETE',
        headers = { 'Authorization' : 'Basic ' + auth ,'Content-Type': 'application/json; charset=UTF-8'}
    )

def put():
    h = httplib2.Http()
    data = dict(code="print 'asd asd'")
    auth = base64.encodestring( 'iye' + ':' + 'asdasd' )
    resp, content = h.request(
        'http://127.0.0.1:8000/snippets/3/',
        'PUT',
        json.dumps(data),
        headers = { 'Authorization' : 'Basic ' + auth ,'Content-Type': 'application/json; charset=UTF-8'}
    )

if __name__ == '__main__' :
    #put()
    #get_all()
    #get()
    h = httplib2.Http()
    resp, content = h.request(
        'http://127.0.0.1:8888/hello',
        'PUT',
    )
    pprint.pprint(json.loads(content))
