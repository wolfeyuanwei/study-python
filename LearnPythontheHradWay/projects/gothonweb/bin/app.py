#!/user/bin/python
#filename:app.py
#-*-coding:utf-8 -*-

import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()