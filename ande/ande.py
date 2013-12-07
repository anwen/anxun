# -*- coding:utf-8 -*-

from anwen.base import BaseHandler
from log import logger


class AndeHandler(BaseHandler):

    def get(self):
        self.render('ande.html')


class EmptyHandler(BaseHandler):

    def get(self, uri):
        logger.info('usersay:%s' % uri)
        self.write('hey~ ლ(◕‿◕)ლ visit <a href="http://x.anwensf.com">anxun</a>')
