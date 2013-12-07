# -*- coding: utf-8 -*-

from ande.ande import AndeHandler
from ande.cache import CacheHandler
from anwen.base import ErrHandler

handlers = [
    (r"/", AndeHandler),
    (r"/cache", CacheHandler),
    (r"/err", ErrHandler),
    (r'/(.*)', AndeHandler),
    # Custom 404 ErrHandler, always put this at last

]
