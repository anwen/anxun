# -*- coding:utf-8 -*-

from anwen.base import BaseHandler
from log import logger
import requests
from requests.exceptions import ConnectionError


class AndeHandler(BaseHandler):

    def get(self):
        self.render('ande.html')


class EmptyHandler(BaseHandler):

    def get(self, uri):
        logger.info('usersay:%s' % uri)
        self.write(
            'hey~ ლ(◕‿◕)ლ visit <a href="http://x.anwensf.com">anxun</a>')


class XHandler(BaseHandler):

    def get(self):
        # , callback='', q='', rsz=8, start=0
        # d = self.get_argument('d', 0)
        atype = self.get_argument('atype', 'web')
        q = self.get_argument('q', '')
        callback = self.get_argument('callback', '')
        rsz = self.get_argument('rsz', 8)
        start = self.get_argument('start', 0)
        if callback:
            callback = 'callback=%s' % callback
        # print self.request.uri
        # http://ajax.googleapis.com/ajax/services/search/web?v=1.0&callback=jQuery1910788396970834583_1422842379032&q=ccc&rsz=8&start=0&_=1422842379033
        self.set_header('Content-Type', 'application/json')
        if not q:
            self.write({'err': 'bad q'})
            return
        xurl = 'http://ajax.googleapis.com/ajax/services/search/%s?v=1.0&%s&q=%s&rsz=%s&start=%s' % (
            atype, callback, q, rsz, start)
        try:
            # for local test
            # proxies = {
            #     'https': 'https://your_ip:your_port',
            #     'http': 'http://your_ip:your_port'
            # }
            proxies = {
                'https': 'https://theironislands.f.getqujing.net:39274',
                'http': 'http://theironislands.f.getqujing.net:39274'
            }
            ret = requests.get(xurl, proxies=proxies, timeout=3)
            # ret = requests.get(xurl, timeout=3)
        except ConnectionError as e:
            self.write({'responseStatus': 'err', 'err': str(e)})
            return
        except Exception as e:
            self.write({'responseStatus': 'err', 'err': str(e)})
            return
        self.write(ret.text)
