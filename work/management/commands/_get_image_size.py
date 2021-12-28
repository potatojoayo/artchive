import urllib
from urllib import request
from PIL import ImageFile


def get_size(uri):

    file = request.urlopen(uri)
    size = file.headers.get('content-length')
    if size:
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return p.image.size
            break
    return size
