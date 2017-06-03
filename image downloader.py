import random

import urllib.request

def image_downloader(url):

    name=random.randrange(1,1000)

    image_name= str(name)+".jpg"

    urllib.request.urlretrieve(url , image_name)



image_downloader("https://i.ytimg.com/vi/5YQkWQbDS9w/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDyDxGLBKIquqABiHvMaIss90lU2g")