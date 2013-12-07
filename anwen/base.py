# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
from utils import random_sayings


class BaseHandler(RequestHandler):

    def get_template_namespace(self):
        ns = super(BaseHandler, self).get_template_namespace()
        ns.update({
            'random_sayings': random_sayings(),
        })
        return ns


class ErrHandler(BaseHandler):

    def get(self):
        self.render('error.html', status_code=404)
