#!/user/bin/python
#filename:setup.py
#-*-coding:utf-8-*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'autor':'wolfe_yuan',
    'url':'URL to get it at.',
    'download_url':'where to download it.',
    'author_email':'wolfe_yuan@163.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)