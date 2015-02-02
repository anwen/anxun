# -*- coding: utf-8 -*-

from ande.ande import AndeHandler, EmptyHandler, XHandler
from ande.cache import CacheHandler
from anwen.base import ErrHandler

handlers = [
    (r"/", AndeHandler),
    (r"/x", XHandler),
    (r"/cache", CacheHandler),
    (r"/=q", CacheHandler),
    (r"/err", ErrHandler),
    (r'/(.*)', EmptyHandler),
    # Custom 404 ErrHandler, always put this at last

]
