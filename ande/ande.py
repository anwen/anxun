# -*- coding:utf-8 -*-

from anwen.base import BaseHandler


class AndeHandler(BaseHandler):

    def get(self):
        self.render('ande.html')
