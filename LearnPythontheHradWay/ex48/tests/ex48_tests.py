#!/user/bin/python
#filename:NAME_tests.py
#-*-coding:utf-8-*-

from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"),[('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])