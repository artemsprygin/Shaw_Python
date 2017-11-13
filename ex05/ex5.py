# -*- coding: utf- 8 -*-

my_name = u'Зед Шоу'
my_age = 35 # это правда!
my_height = 188 # см
my_weight = 80 # кг
my_eyes = u'Голубые'
my_teeth = u'Белые'
my_hair = u'Каштановые'

print u"Давайте поговорим о человеке по имени %s." % my_name
print u"Его рост составляет %d см." % my_height
print u"Он весит %d кг." % my_weight
print u"На самом деле это не так и много."
print u"У него %s глаза и %s волосы." % (my_eyes, my_hair)
print u"Его зубы обычно %s, хотя он и любит пить кофе." % my_teeth

# эта строка кода довольно сложная, не ошибитесь!
print u"Если я сложу %d, %d и %d, то получу %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)