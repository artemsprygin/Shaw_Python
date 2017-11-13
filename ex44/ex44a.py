# -*- coding: utf- 8 -*-


class Parent(object):

	def implicit(self):
		print u"РОДИТЕЛЬ implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()