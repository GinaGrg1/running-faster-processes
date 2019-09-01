import struct
import zmq

"""
First start the server:
    $ python3 geo_server_using_zmq.py
    
"""
ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect('tcp://localhost:7000')

lat1, lng1 = 34.3852712, -119.487444  # Recording booth
lat2, lng2 = 37.7765072, -122.3942272  # Dropbox HQ (where Guido works)

msg = struct.pack('>dddd', lat1, lng1, lat2, lng2)  # encode the floats into a bytre stream
sock.send(msg)
data = sock.recv()
dist, = struct.unpack('>d', data)  # unpack the byte stream to one single float
print('distance = {:.2f}'.format(dist))

