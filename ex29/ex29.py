# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15


if people < cats:
	print u"Слишком много кошек! Мир обречен!"

if people > cats:
	print u"Не так много кошек! Мир спасен!"

if people < dogs:
	print u"Мир утоп в слюнях!"

if people > dogs:
	print u"Мир сухой!"


dogs += 5

if people >= dogs:
	print u"Людей больше или столько же, сколько собак."

if people <= dogs:
	print u"Людей меньше или столько же, сколько собак."


if people == dogs:
	print u"Людей столько же, сколько собак."
