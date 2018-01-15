#!/usr/bin/python
#filename:toolbox.py

def openAnything(source):
    if hasattr(source, "read"):
        return source
    if source == '-':
        import sys
        return sys.stdin
    import urllib
    try:
        return urllib.urlopen(source)
    except (IOError, OSError):
        pass
    try:
        return open(source)
    except (IOError, OSError):
        pass
    import StringIO
    return StringIO.StringIO(str(source))