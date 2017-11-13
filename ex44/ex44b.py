# -*- coding: utf- 8 -*-


class Parent(object):

	def override(self):
		print u"РОДИТЕЛЬ override()"

class Child(Parent):

	def override(self):
		print u"ПОТОМОК override()"

dad = Parent()
son = Child()

dad.override()
son.override()