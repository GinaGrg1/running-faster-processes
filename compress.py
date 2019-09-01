from flask import Flask, Response, request
import gzip

"""
Start the server:
    $ python3 compress.py
Check in the browser:
    http://localhost:8080/sherlock
    http://localhost:8080/sherlockc
To benchmark:
    $ wrk -s wrk.lua http://localhost:8080/sherlock  # for uncompressed
    $ wrk -s wrk.lua http://localhost:8080/sherlockc
"""

app = Flask(__name__)
ctype = 'text/plain; charset=utf-8'

with open('./data/sherlock-holmes.txt', 'rb') as fp:
    data = fp.read()

zdata = gzip.compress(data)


@app.route('/sherlock')
def sherlock():
    # this a handler which returns the data uncompressed
    resp = Response(data, content_type=ctype)
    resp.headers['Connection'] = 'close'
    return resp


@app.route('/sherlockc')
def sherlockc():
    if 'gzip' not in request.headers.get('Accept-Encoding', ''):  # check if client can accept a compressed data
        return data

    resp = Response(zdata, content_type=ctype)
    resp.headers['Content-Encoding'] = 'gzip'
    resp.headers['Connection'] = 'close'
    return resp


if __name__ == '__main__':
    app.run(port=8080)
