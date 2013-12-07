# -*- coding:utf-8 -*-

from anwen.base import BaseHandler
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.web import asynchronous
from tornado.httpclient import HTTPRequest
from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncHTTPClient
from urlparse import urlparse
from log import logger


class CacheHandler(BaseHandler):

    @asynchronous
    def get(self):
        # q = self.get_argument('q', '') # raise UnicodeDecodeError
        print(self.request.uri)
        if '/cache?q=' in self.request.uri:
            q = self.request.uri.replace('/cache?q=', '')
        if '/=q?q=' in self.request.uri:
            q = self.request.uri.replace('/=q?q=', '')
        s = self.get_argument('s', '')
        if s == '1':
            s = 'http://cn.nytimes.com/opinion/20131207/c07kristof/'
        if s == '2':
            s = 'http://www.youtube.com/?hl=zh-CN'
        if q:
            q = q[::-1]
        if s:
            q = s
        if not q:
            self.write('you find nothing')
        print(q)
        headers = dict(self.request.headers)
        headers["Host"] = urlparse(q).netloc
        self.q = q
        try:
            AsyncHTTPClient().fetch(
                HTTPRequest(url=q,
                            method="GET",
                            # body=self.request.body,
                            headers=headers,
                            follow_redirects=True),
                self._on_proxy)
        except tornado.httpclient.HTTPError as x:
            if hasattr(x, "response") and x.response:
                self._on_proxy(x.response)
            else:
                err = "Tornado signalled HTTPError %s" % x
                logger.error(err)
                self.render('error.html', status_code=err)

    def _on_proxy(self, response):
        if response.error is not None:
            # print(type(response.error))
            err = str(response.error)
            logger.error(err)
            self.render('error.html', status_code=err)
        else:
            self.set_status(response.code)
            for header in (
                    "Date", "Cache-Control",
                    "Server", "Content-Type", "Location"):
                v = response.headers.get(header)
                if v:
                    self.set_header(header, v)
            if response.body:
                domain = '{uri.scheme}://{uri.netloc}/'.format(
                    uri=urlparse(self.q))
                body = response.body
                import re
                url_re = re.compile('href="/(?!/)')
                body = url_re.sub("href=\"%s" % domain, body)
                self.write(body)
            self.finish()
