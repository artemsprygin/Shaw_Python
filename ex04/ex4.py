# -*- coding: utf- 8 -*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print u"В наличии", cars, u"автомобилей."
print u"И только", drivers, u"водителей вышли на работу."
print u"Получается, что", cars_not_driven, u"машин пустуют."
print u"Мы можем перевезти сегодня", carpool_capacity, u"человек."
print u"Сегодня нужно отвезти", passengers, u"человек."
print u"В каждой машине будет примерно", average_passengers_per_car, u"человека."