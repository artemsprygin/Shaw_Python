# -*- coding: utf- 8 -*-


class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = []

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

		
		central_corridor = Room("Central Corridor",
"""
Готоны с планеты Перкаль 25 захватили ваш корабль и уничтожили 
всю команду.  Вы - единственный, кто остался в живых. 
Вам нужно выкрасть нейтронную бомбу в оружейной лаборатории, 
заложить ее в топливном отсеке и покинуть корабль в спасательной 
капсуле  прежде, чем он взорвется.

Вы бежите по центральному коридору в оружейную лабораторию, когда перед вами 
появляется Готон с красной чешуйчатой кожей, гнилыми зубами и в костюме клоуна. 
Он с ненавистью смотрит на вас и, перегородив дорогу в лабораторию, 
вытаскивает бластер, чтобы уничтожить вас.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
К счастью, вы знакомы с культурой Готонов и знаете, что их способно рассмешить. 
Вы рассказываете бородатый анекдот: 
Неоколонии, изоморфно релятивные к мyльтиполосным гиперболическим параболоидам. 
Готон замирает, старается сдержать смех, а затем начинает безудержно хохотать. 
Пока он смеется, вы достаете бластер и стреляете Готону в голову. 
Он падает, а вы перепрыгиваете его и бежите в оружейную лабораторию.

Вы вбегаете в оружейную лабораторию и начинаете обыскивать комнату, 
спрятались ли тут другие Готоны.  Стоит мертвая тишина. 
Вы бежите в дальний угол комнаты и находите нейтронную бомбу 
в защитном контейнере. На лицевой стороне контейнера расположена 
панель с кнопками и вам надо ввести правильный код, чтобы достать бомбу. 
Если вы 10 раз введете неправильный код, контейнер заблокируется и вы 
не сможете достать бомбу.  Код состоит из трех цифр.
""")


the_bridge = Room("The Bridge",
"""
Контейнер открывается со щелчком и выпускает сизый газ. 
Вы вытаскиваете нейтронную бомбу и бежите в топливный отсек, 
чтобы установить бомбу в нужном месте.

Вы вбегаете в топливный отсек с нейтронной бомбой и видите 
пятерых Готонов, безуспешно пытающихся управлять 
кораблем.  Один уродливее другого и все в клоунских 
костюмах, как и Готон, убитый вами.  Они не достают оружие, 
так как видят бомбу у вас в руках и не хотят, чтобы 
вы установили ее.
""")


escape_pod = Room("Escape Pod",
"""
Вы указываете бластером на бомбу в ваших руках. 
Готоны поднимают лапы вверх и в страхе потеют. 
Вы осторожно, не отворачиваясь, подходите к двери и 
аккуратно устанавливаете бомбу, держа Готонов под прицелом. 
Вы запрыгиваете в шлюз и закрываете ее ударом по кнопке, 
а затем бластером расплавляете замок, чтобы Готоны не смогли 
открыть дверь. Теперь вам нужно залезть в спасательную капсулу 
и удрать с корабля к чертям собачьим.

Вы мчитесь по отсеку со спасательными капсулами. Некоторые из них 
могут быть повреждены и взорвутся во время полета. Всего капсул 
пять и у вас нет времени, чтобы осматривать каждую из них 
на отсутствие повреждений. 
Задумавшись на секунду, вы решаете сесть в капсулу под 
номером... 
Какой номер вы выбираете?
""")


the_end_winner = Room("The End",
"""
Вы запрыгиваете в капсулу номер 2 и нажимаете кнопку отстыковки. 
Капсула вылетает в космическое пространство, а затем "
отправляется к планете неподалеку. Вы смотрите в иллюминатор и видите, как ваш 
корабль взрывается. Его осколки повреждают топливный отсек корабля 
Готонов и тот тоже разлетается в клочья. 
Победа за вами!
""")


the_end_loser = Room("The End",
"""
Вы запрыгиваете в капсулу со случайным номером и нажимаете кнопку отстыковки. 
Капсула вылетает в космическое пространство, а затем 
взрывается с яркой вспышкой и разбрасывая осколки. 
Вы умираете.
"""
)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.") # Вы умерли

the_bridge.add_paths({
    'throw the bomb': generic_death, # бросить бомбу
    'slowly place the bomb': escape_pod # установить бомбу
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death, # стрелять!
    'dodge!': generic_death, # проскочить!
    'tell a joke': laser_weapon_armory # пошутить!
})

START = central_corridor