# -*- coding: utf- 8 -*-


class Parent(object):

	def override(self):
		print u"РОДИТЕЛЬ override()"

	def implicit(self):
		print u"РОДИТЕЛЬ implicit()"

	def altered(self):
		print u"РОДИТЕЛЬ altered()"

class Child(Parent):

	def override(self):
		print u"ПОТОМОК override()"

	def altered(self):
		print u"ПОТОМОК, ДО ВЫЗОВА altered() В РОДИТЕЛЕ"
		super(Child, self).altered()
		print u"ПОТОМОК, ПОСЛЕ ВЫЗОВА altered() В РОДИТЕЛЕ"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
