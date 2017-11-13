# -*- coding: utf- 8 -*-
import codecs, sys
outf = codecs.getwriter('cp866')(sys.stdout, errors='replace')
sys.stdout = outf

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print u"Эта сцена еще не настроена. Создайте подкласс и реализуйте функцию enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # не забудьте вывести последнюю сцену
        current_scene.enter()

class Death(Scene):

    quips = [
        u"Вы погибли.  Как это ни печально.",
        u"Ваша мать будет грустить по вам... надо было быть умнее.",
        u"Надо же было быть таким придурком.",
        u"Даже мой маленький щенок соображает лучше."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print u"Готоны с планеты Перкаль 25 захватили ваш корабль и уничтожили "
        print u"всю команду.  Вы - единственный, кто остался в живых. "
        print u"Вам нужно выкрасть нейтронную бомбу в оружейной лаборатории, "
        print u"заложить ее в топливном отсеке и покинуть корабль в спасательной "
        print u"капсуле  прежде, чем он взорвется."
        print "\n"
        print u"Вы бежите по центральному коридору в оружейную лабораторию, когда перед вами "
        print u"появляется Готон с красной чешуйчатой кожей, гнилыми зубами и в костюме клоуна. "
        print u"Он с ненавистью смотрит на вас и, перегородив дорогу в лабораторию, "
        print u"вытаскивает бластер, чтобы уничтожить вас."

        action = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

        if action == u"стрелять!":
            print u"Вы быстро выхватываете свой бластер и начинаете палить по Готону. "
            print u"Его клоунский наряд крутится вокруг тела, мешая лучам попадать в "
            print u"его тело.  Все ваши выстрелы лазером потерпели неудачу и заряд бластера иссяк. "
            print u"Костюм Готона, который купила его мать, безнадежно испорчен, поэтому "
            print u"он в ярости выхватывает бластер и стреляет вам в голову."
            print u"Вы убиты."
            return 'death'

        elif action == u"проскочить!":
            print u"Словно боксер мирового класса, вы уворачиваетесь и проскальзываете справа "
            print u"от Готона, краем глаза видя, что его бластер направлен вам в голову. "
            print u"И тут вы подскальзываетесь и врезаетесь в металлическую стену. От удара "
            print u"вы теряете сознание. "
            print u"Придя в сознание, вы успеваете почувствовать, что Готон топчется на вашей "
            print u"голове и пожирает вас."
            return 'death'

        elif action == u"пошутить!":
            print u"К счастью, вы знакомы с культурой Готонов и знаете, что их способно рассмешить. "
            print u"Вы рассказываете бородатый анекдот: "
            print u"Неоколонии, изоморфно релятивные к мyльтиполосным гиперболическим параболоидам. "
            print u"Готон замирает, старается сдержать смех, а затем начинает безудержно хохотать. "
            print u"Пока он смеется, вы достаете бластер и стреляете Готону в голову. "
            print u"Он падает, а вы перепрыгиваете его и бежите в оружейную лабораторию."
            return 'laser_weapon_armory'

        else:
            print u"ТАК НЕЛЬЗЯ ПОСТУПИТЬ!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print u"Вы вбегаете в оружейную лабораторию и начинаете обыскивать комнату, "
        print u"спрятались ли тут другие Готоны.  Стоит мертвая тишина. "
        print u"Вы бежите в дальний угол комнаты и находите нейтронную бомбу "
        print u"в защитном контейнере. На лицевой стороне контейнера расположена "
        print u"панель с кнопками и вам надо ввести правильный код, чтобы достать бомбу. "
        print u"Если вы 10 раз введете неправильный код, контейнер заблокируется и вы "
        print u"не сможете достать бомбу.  Код состоит из трех цифр."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print u"ВЖЖЖИИИК!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print u"Контейнер открывается со щелчком и выпускает сизый газ. "
            print u"Вы вытаскиваете нейтронную бомбу и бежите в топливный отсек, "
            print u"чтобы установить бомбу в нужном месте."
            return 'the_fuelcell'
        else:
            print u"Вы слышите, как замок жужжит последний раз, а затем чувствуете "
            print u"горелый запах - замок расплавился. "
            print u"Вы остаетесь в оружейной лавке, пока наконец Готоны не взорвут "
            print u"ваш корабль со своего, и вы не умрете."
            return 'death'



class TheFuelcell(Scene):

    def enter(self):
        print u"Вы вбегаете в топливный отсек с нейтронной бомбой и видите "
        print u"пятерых Готонов, безуспешно пытающихся управлять "
        print u"кораблем.  Один уродливее другого и все в клоунских "
        print u"костюмах, как и Готон, убитый вами.  Они не достают оружие, "
        print u"так как видят бомбу у вас в руках и не хотят, чтобы "
        print u"вы установили ее."

        action = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

        if action == u"бросить бомбу":
            print u"Вы в панике активируете и бросаете бомбу в толпу Готонов, "
            print u"а затем прыгаете к двери шлюза.  Сразу после этого "
            print u"один из Готонов стреляет вам в спину. Умирая, "
            print u"вы видите, как другие Готоны тщетно пытаются деактивировать "
            print u"бомбу. Умирая, вы осознаете, что Готоны тоже погибнут."
            print u"Ваше сознание угасает."
            return 'death'

        elif action == u"установить бомбу":
            print u"Вы указываете бластером на бомбу в ваших руках."
            print u"Готоны поднимают лапы вверх и в страхе потеют."
            print u"Вы осторожно, не отворачиваясь, подходите к двери и "
            print u"аккуратно устанавливаете бомбу, держа Готонов под прицелом. "
            print u"Вы запрыгиваете в шлюз и закрываете ее ударом по кнопке, "
            print u"а затем бластером расплавляете замок, чтобы Готоны не смогли "
            print u"открыть дверь. Теперь вам нужно залезть в спасательную капсулу "
            print u"и удрать с корабля к чертям собачьим."
            return 'escape_pod'
        else:
            print u"ТАК НЕЛЬЗЯ ПОСТУПИТЬ!"
            return "the_fuelcell"


class EscapePod(Scene):

    def enter(self):
        print u"Вы мчитесь по отсеку со спасательными капсулами. Некоторые из них "
        print u"могут быть повреждены и взорвутся во время полета. Всего капсул "
        print u"пять и у вас нет времени, чтобы осматривать каждую из них "
        print u"на отсутствие повреждений."
        print u"Задумавшись на секунду, вы решаете сесть в капсулу под "
        print u"номером... "
        print u"Какой номер вы выбираете?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print u"Вы запрыгиваете в капсулу номер %s и нажимаете кнопку отстыковки." % guess
            print u"Капсула вылетает в космическое пространство, а затем "
            print u"взрывается с яркой вспышкой и разбрасывая осколки."
            print u"Вы умираете."
            return 'death'
        else:
            print u"Вы запрыгиваете в капсулу номер %s и нажимаете кнопку отстыковки." % guess
            print u"Капсула вылетает в космическое пространство, а затем "
            print u"отправляется к планете неподалеку.  Вы смотрите в иллюминатор и видите, как ваш "
            print u"корабль взрывается. Его осколки повреждают топливный отсек корабля "
            print u"Готонов и тот тоже разлетается в клочья. "
            print u"Победа за вами!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print u"Вы победили! Отличная работа!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_fuelcell': TheFuelcell(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()		