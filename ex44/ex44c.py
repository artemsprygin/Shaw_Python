# -*- coding: utf- 8 -*-


class Parent(object):

	def altered(self):
		print u"РОДИТЕЛЬ altered()"

class Child(Parent):

	def altered(self):
		print u"ПОТОМОК, ДО ВЫЗОВА altered() В РОДИТЕЛЕ"
		super(Child, self).altered()
		print u"ПОТОМОК, ПОСЛЕ ВЫЗОВА altered() В РОДИТЕЛЕ"

dad = Parent()
son = Child()

dad.altered()
son.altered()
