#!/user/bin/python
#filename:app1.py
#-*-coding:utf-8 -*-

import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()