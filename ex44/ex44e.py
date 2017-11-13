# -*- coding: utf- 8 -*-


class Other(object):

	def override(self):
		print u"КЛАСС OTHER, override()"

	def implicit(self):
		print u"КЛАСС OTHER, implicit()"

	def altered(self):
		print u"КЛАСС OTHER, altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print u"ПОТОМОК override()"

	def altered(self):
		print u"ПОТОМОК, ДО ВЫЗОВА altered() В КЛАССЕ OTHER"
		self.other.altered()
		print u"ПОТОМОК, ПОСЛЕ ВЫЗОВА altered() В КЛАССЕ OTHER"

son = Child()

son.implicit()
son.override()
son.altered()