#!/usr/bin/python
#filename:openanything.py
import urllib2, urlparse,gzip
from StringIO import StringIO
USER_AGENT='OpenAnything/1.0 +http://diveintopython.org/http_web_services/'
class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(
            self, req, fp, code, msg, headers)
        result.status = code
        return result
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)
        result.status = code
        return result

class DefaultErrorHandler(urllib2.HTTPRedirectHandler):
    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(
            req.get_full_url(), code, msg, headers, fp)
        result.status = code
        return result

def openAnything(source, etag=None, lastmodified=None, agent=USER_AGENT):
    '''URL, filename, or string -->stream
    This function lets you define parsers tha take any input source
    (URL, pathname to local or network file, or actual data as a string)
    and deal with it in a uniform manner. Returned object is guaranteed
    to have all the basic stdio read methods(read, readline, readlines).
    Just .close() the object when you're done with it.
    If the etag argument is supplied, it will be used as the value of an
    If-None-Match request header.
    If the lastmodified argument is supplied, it must be a formatted
    date/time string in GMT(as returned in the Last-Modified header of
    a previous request)'''
    if hasattr(source, 'read'):
        return source
    if source == '-':
        return sys.stdin
    if urlparse.urlparse(source)[0] == 'http':
        request = urllib2.Request(source)
        request.add_header('User-Agent', agent)
        if etag:
            request.add_header('If-Modified-Since', lastmodified)
        request.add_header('Accept-encoding','gzip')
        opener=urllib2.build_opener(SmartRedirectHandler(), DefaultErrorHandler())
        return opener.open(request)
    try:
        return open(source)
    except (IOError, OSError):
        pass
    return StringIO(str(source))

def fetch(source, etag=None, last_modified=None, agent=USER_AGENT):
    '''Fetch data and metadata from a URL, file stream, or string'''
    result={}
    f=openAnything(source, etag, last_modified, agent)
    result['data']=f.read()
    if hasattr(f, 'headers'):
        result['etag']=f.headers.get('ETag')
        result['lastmodified']=f.headers.get('Last-Modified')
        if f.headers.get('content-endoding', '') == 'gzip':
            result['data']=gzip.GzipFile(fileobj=StringIO(result['data'])).read()
    if hasattr(f, 'url'):
        result['url']=f.url
        result['status']=200
    if hasattr(f, 'status'):
        result['status']=f.status

    f.close()
    return result