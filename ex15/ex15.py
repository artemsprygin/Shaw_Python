# -*- coding: utf- 8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print u"Содержимое файла %r:" % filename
print txt.read()

print u"Введите имя файла снова:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()