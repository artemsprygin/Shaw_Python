# -*- coding: utf- 8 -*-

from nose.tools import *
import NAME

def setup():
    print u"УСТАНОВКА!"

def teardown():
    print u"ЗАВЕРШЕНИЕ!"

def test_basic():
    print u"ВЫПОЛНЕНИЕ!"