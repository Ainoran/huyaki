# game_for_Daria

import random as r
from colorama import init
from colorama import Fore
import sys
init()


def initgame():
    global health, money, damage, critch,  map, keygirl, ctticket, meetmap, armor, enemycounter, armor, enemylvldefined,\
        inventory, fighthealing, meetshop1, maptoct, mvinit, mvvars
    global mv1, mv2, mv3, mv4, mv5, mv6, mv7, mv8, mv9, mv10, mv11, mv12, mv13, mv14, mv15, mv16, mv17, mv18, mv19, mv20
    #definders
    enemylvldefined = 0

    #stats
    map = 0
    critch = 10
    maxhealth = 25
    health = 10
    money = 700
    damage = 2
    enemycounter = 0
    armor = 0

    #evetntskeys
    keygirl = 0
    ctticket = 0
    meetmap = 0
    maptoct = 0
    meetshop1 = 0

    #fights
    fighthealing = 0


    #inventory
    inventory = []

    #mvinit
    mv1 = (
            Fore.BLUE + "Ты видишь небольшой храм или святилище посреди леса. Здесь можно хорошо отдохнуть и восстановить силы.")
    mv2 = (Fore.BLUE + "Наступила плохая погода. В густых тропинках ты не заметила корень дерева и споткнулся об него.")
    mv3 = (Fore.BLUE + 'Ты встретила сундук посредине поляны, рядом была табличка с надписью: "Впереди - мимик"')
    mv4 = (Fore.BLUE + 'Ты встретила сундук посредине поляны, рядом была табличка с надписью: "Впереди - не мимик"')
    mv5 = (Fore.BLUE + "Ты понимаешь, что третий раз выходишь на одно и то же место.")
    mv6 = (Fore.BLUE + "Ты увидела бледную женщину в белом платье за одним из деревьев.")
    mv7 = (
            Fore.BLUE + "Перед тобой женщина, это охотница, вышедшая проверить силки. Она угодила в ловушку и просит о помощи.")
    mv8 = (Fore.BLUE + "Странные следы пересекают твой путь - такое ощущение, что прошёл кто-то весом несколько тонн")
    mv9 = (Fore.BLUE + "На одном из деревьев ты увидела листовку с надписью 'Ведётся набор в маги-ученики'")
    mv10 = (Fore.BLUE + "Ты видишь руины башни, здесь вполне можно остановиться на ночлег.")
    mv11 = (
            Fore.BLUE + "Среди деревьев стоит заброшенная лачуга, вид которой не вызывает никаких положительных эмоций.")
    mv12 = (Fore.BLUE + "Ты наткунлась на деревню. Звучит так будто в ней никого нет. Или точнее... Не звучит?")
    mv13 = (Fore.BLUE + "Ты учуяла запах жареного мяса совсем близко.")
    mv14 = (Fore.BLUE + "Остановившись на пару секунд чтобы отдохнуть, ты почувствовала, что на тебя кто-то смотрит")
    mv15 = (Fore.BLUE + "Ты вышла из леса и увидела перед собой тропу ведущую в огромную крепость")
    mv16 = (Fore.BLUE + "Ты увидела отблеск в земле. Подойдя ближе ты поняла, что это закопанное НЛО.")
    mv17 = (Fore.BLUE + "Ты увидела как кто-то нацарапал «9,3,7» на дереве и превратился в прах.")
    mv18 = (Fore.BLUE + "Услышав жужание ты резко осознала, что вокруг тебя чертовски много пчел...")
    mv19 = (Fore.BLUE + "Внезапно ты почувствовала жуткую усталость. Вокруг тебя совсем тихо и только деревья.")
    mv20 = (
            Fore.BLUE + "Из ниоткуда подошла девочка и спросила" + Fore.WHITE + "\n-Тётенька, а это не вы меня спасли тогда?")

    #gamedescstart
    input(Fore.GREEN + username + ' ты проснулась на опушке леса и пошла куда глаза глядят')
    showparameters()
    showmap()
    gameproc()


print(Fore.RED + "Инструкция.")
print('Если вам не задаётся вопрос, жмите Enter чтобы продолжить повествование')
print(
    'Если вам задаётся вопрос, то ответом на него будут являться слова в скобках (если имеются), либо слово "да"(Да,дА,ДА,да, без разницы)')
print('Любой другой ответ будет распознан как "нет", даже если вы написали "ага","дап","ад" или не написали ничего')
print(
    'Также хочу отметить, что урон не складывается (изначально у вас 2 урона, купив меч на 6 урона вы будете иметь 6 урона)')
print(
    Fore.YELLOW + 'Механики боя: блок - режет урон противника в 2 раза и с шансом 50% наносит 1 единицу урона, но есть 20% шанса поставить его неправильно')
print('Контратака - 40% шанс увернуться от атаки противника и нанести ему от 2 до 3 единиц урона')
print('Побег - 20% шанс на то чтобы сбежать из боя (как по мне, очень бесполезно, но я решил добавить это в игру)')
print('Мощная атака - при нанесении удара есть определенный шанс на удвоение урона. Изначально шанс составляет 10%')
print(Fore.BLUE + 'На этом вроде все. Удачной игры.')
username = input(Fore.GREEN + 'Введи свое имя: ')
input("Привет " + username + ", по сюжету ты просыпаешься в густом лесу мира фентези, пытаешься выжить и попасть обратно в реальный мир")

class Potion:




    def __init__(self,name='Зелье здоровья',lvl=0, v1=0, v2=0):
        self.name = name
        self.lvl = lvl
        self.value1 = v1
        self.cost = v2

    def gener(self):
        self.lvl = r.randint(1, 3)
        self.cost = r.randint(10, 15) * self.lvl
        self.value1 = self.lvl + r.randint(1, 2)
    def generctmerch(self):
        self.lvl = r.randint(2, 5)
        self.cost = r.randint(15, 24) * self.lvl
        self.value1 =self.lvl + r.randint(2, 3)
class Weapon():
    def __init__(self, lvl=0, name='emty', v1=0, v2=0, v3=0, v4=0):
        self.name = name
        self.lvl = lvl
        self.damage = v1
        self.crit = v2
        self.cost = v3
        self.isbought = v4
    def weapondesc(self):
        print('{0}. У него {1} урона и {2}% шанса крита.'.format(self.name, self.damage, self.crit))
    def gener(self):
        weaponsnames = [' меч', " посох", " кинжал", ' гусь', ' лук']  # ГЕНЕРАЦИЯ ОРУЖИЯ
        weaponlvl = r.randint(1, 3)
        weaponrars = ['Дряхлый', "Простой", 'Прочный']

        self.lvl=weaponlvl
        self.name=weaponrars[weaponlvl-1]+r.choice(weaponsnames)
        self.damage=weaponlvl*1.5+0.5
        self.crit=r.randint(10, 20) +r.randint(1, 5)*weaponlvl
        self.cost=r.randint(20, 30)*weaponlvl
        self.isbought = 0
    def genercommonmerch(self):
        weaponsnames = [' меч', " посох", " кинжал", ' гусь', ' лук']  # ГЕНЕРАЦИЯ ОРУЖИЯ
        weaponlvl = r.randint(1, 3)
        weaponrars = ['Дряхлый', "Простой", 'Прочный']

        self.lvl = weaponlvl
        self.name = weaponrars[weaponlvl - 1] + r.choice(weaponsnames)
        self.damage = weaponlvl * 1.5 + 0.5
        self.crit = r.randint(10, 20) + r.randint(1, 5) * weaponlvl
        self.cost = r.randint(20, 30) * weaponlvl
        self.isbought = 0
    def generctmerch(self):
        weapons = ["Скимитар", "Копьё", "Рапира", "Боевой топор", "Шашка", "Длинный лук", "Булава", "Двуручный меч"]
        weaponlvl = r.randint(1, 5)
        weaponrars = [' рядового', " сержанта", ' офицера', ' генерала', " героя"]
        self.lvl = weaponlvl
        self.name = r.choice(weapons)+weaponrars[weaponlvl - 1]
        self.damage = weaponlvl * 2.5
        self.crit = r.randint(20, 30) + r.randint(1, 5) * weaponlvl
        self.cost = r.randint(30, 45) * weaponlvl
        self.isbought = 0
    def genertrollmerch(self):
        weapons = [' бивень мамонта', " зуб тигра", " коготь дракона"]
        weaponlvl = r.randint(1, 5)
        weaponrars = ['Обгрызлый', "Украденный", 'Пыльный', 'Отличный', "Заточенный"]
        self.lvl = weaponlvl
        self.name = weaponrars[weaponlvl - 1]+r.choice(weapons)
        self.damage = weaponlvl * 3.5
        self.crit = r.randint(5, 12)
        self.cost = r.randint(40, 65) * weaponlvl
        self.isbought = 0
class Armor():

    def __init__(self,name='epmty',lvl=0, v1=0, v2=2, v3=0,v4=0):
        self.name = name
        self.lvl = lvl
        self.armor = v1
        self.cost = v2
        self.blockch = v3
        self.isbought = v4
    def gener(self):
        armors = ['доспех', 'нагрудник', 'кольчуга', 'бригантина']  # ГЕНЕРАЦИЯ БРОНИ
        armorlvl = r.randint(1, 3)
        armorrars = ['Поношенн', 'Обычн', 'Укрепленн']
        armorrar = armorrars[armorlvl - 1]
        armend = ['ый', 'ая']
        armordec = r.randint(0, 3)
        armorname1 = armors[armordec]
        if armordec < 2:
            armorname2 = armend[0]
        else:
            armorname2 = armend[1]
        self.name = armorrar + armorname2 + ' ' + armorname1
    def genercommonmerch(self):
        armors = [' гамбезон', ' нагрудник', ' стёганка', ' рубашка']  # ГЕНЕРАЦИЯ БРОНИ
        armorlvl = r.randint(1, 3)
        armorrars = ['Поношенн', 'Обычн', 'Укрепленн']
        armorrar = armorrars[armorlvl - 1]
        armend = ['ый', 'ая']
        armordec = r.randint(0, 3)
        armorname1 = armors[armordec]
        if armordec < 2:
            armorname2 = armend[0]
        else:
            armorname2 = armend[1]
        self.name = armorrar + armorname2 + ' ' + armorname1
        self.armor = 0.5 * armorlvl
        self.cost = r.randint(30, 50) * armorlvl
        self.isbought = 0
    def generctmerch(self):
        armors = [' доспех', ' нагрудник', ' кольчуга', ' бригантина',' латы']  # ГЕНЕРАЦИЯ БРОНИ
        armorlvl = r.randint(2, 5)

        armorrars = ['Обычн', 'Прочн', 'Солдатск', 'Генеральск']
        armorrar = armorrars[armorlvl - 2]
        armend = ['ый', 'ий', 'ая', 'ые']
        armordec = r.randint(0, 4)
        armorname1 = armors[armordec]
        if armordec <2:                           #ОПРЕДЕЛЕНИЕ ОКОНЧАНИЯ
            if armorlvl<4:
                armorname2 = armend[0]
            else:
                armorname2 = armend[1]
        elif armordec ==4:
            armorname2 = armend[3]
        else:
            armorname2 = armend[1]
        self.name = armorrar + armorname2 + ' ' + armorname1
        self.armor = 0.5 * armorlvl + (r.randint(1,2)/2)
        self.cost = r.randint(40, 60) * armorlvl
        self.isbought = 0
def showparameters():
    global health
    global money
    global damage
    global map
    input(Fore.YELLOW + 'У тебя {0} жизней, {1} монет \nТы нансоишь {2} урона, имея {3}% шанса крита \nУ тебя {4} брони'.format(health, money,damage, critch, armor))


def showhp():
    global health
    input(Fore.YELLOW + 'Сейчас у тебя {0} жизней'.format(health))


def showcrit():
    global critch
    input(Fore.YELLOW + 'Сейчас у тебя {0}% шанса крита'.format(critch))


def showmap():
    global map
    if map == 0:
        print('У тебя нет карты')
    elif map == 1:
        print("у тебя есть карта")


def showec():
    global enemycounter
    input(Fore.YELLOW + 'Тобой убито {0} противников'.format(enemycounter))


def showmoney():
    global money
    input(Fore.YELLOW + 'Сейчас у тебя {0} монет'.format(money))


def showdmg():
    global damage
    global critch
    input(Fore.YELLOW + 'Теперь у тебя {0} урона и {1}% шанса крита'.format(damage, critch))


def showarm():
    global armor
    input(Fore.YELLOW + 'Теперь у тебя {0} брони'.format(armor))


def showinv():
    global inventory
    for i in range(len(inventory)):
        print(Fore.LIGHTWHITE_EX +str(i+1)+') '+inventory[i].name + ' '+str(inventory[i].lvl)+' уровня')
    print(Fore.LIGHTWHITE_EX +str(len(inventory)+1)+') Выйти из рюкзака')

def showwin():
    global money
    global health
    input(Fore.YELLOW + 'Сейчас у тебя {0} монет и {1} жизней'.format(money, health))


def buy(cost):
    global money
    if money >= cost:
        money -= cost
        print(Fore.YELLOW+"У тебя остaлось {} монет".format(money))
        return True
    print(Fore.RED + "У тебя нет таких денег.")
    return False


def getting():
    global enemyac
    global dodge
    global armor
    global health
    global enemylvl
    global enemyhp
    global money
    global enemydamage
    global enemycounter, ctticket, fightisgoing
    enemyac = r.randint(1, 10)
    if enemyac >= (3):
        health -= enemydamage
        if health > int(0):
            if enemydamage==0:
                input(Fore.BLUE +'{0} не смог пробить твою защиту'.format(enemyname))
            else:
                input(Fore.RED + enemyname + " ударил тебя на {}. У тебя теперь {} жизней".format(enemydamage,
                                                                                              health))
        if health <= 0:
            input(Fore.RED + enemyname + " нанес сокрушительный удар. Ты погибла.")
            fightisgoing = False
    elif enemyac <= (2):
        enemyhp += r.randint(1, 3)
        input(Fore.GREEN + enemyname + ' решил переждать и восстановиться. Теперь у него {0} жизней'.format(
            enemyhp))


def fight():
    global enemyname
    global money
    global damage
    global health
    global enemyac
    global enemylvl
    global enemylvldefined
    global enemyhp
    global enemydamage
    global dodge
    global armor
    global critch, inventory, fighthealing, ctticket, enemycounter, fightisgoing



    if enemylvldefined == 0:
        if ctticket == 0:
            enemylvl = r.randint(1, 4)
            loot = r.randint(10, 20) * enemylvl
            enemydamage = (r.randint(1, 2) * enemylvl / 2) - armor
            enemyhp = r.randint(1, 3) * enemylvl + 1
        elif ctticket == 1:
            enemylvl = r.randint(1, 8)
            loot = r.randint(20, 30) * enemylvl
            enemydamage = (r.randint(2, 3) * enemylvl / 2) - armor
            enemyhp = r.randint(2, 4) * enemylvl + 2
    else:
        enemylvldefined = 0
        loot = r.randint(15, 25) * enemylvl
        enemydamage = (r.randint(1, 2) * enemylvl / 2) - armor
        enemyhp = r.randint(1, 3) * enemylvl + 2
    enemyac = r.randint(1, 10)

    if enemydamage <0.5:
        enemydamage = 0
    input(Fore.RED + "Перед тобой {0} {1} уровня, у него {2} здоровья.".format(enemyname, enemylvl, enemyhp))
    fightisgoing = True
    while fightisgoing:
        if enemyhp > 0:
            dodge = 0
            print(Fore.GREEN + "Твои действия?")
            print(Fore.CYAN + '1) Нанести удар')
            print('2) Поставить блок')
            print('3) Провести контратаку')
            print('4) Попытаться сбежать')
            if len(inventory)>=1:
                print('5) Выпить зелье здоровья из рюкзака')
            actpl = input()
            if actpl == '1':
                punchchance = r.randint(1, 100)
                if punchchance >= 11:
                    critreal = r.randint(1, 100)
                    if critreal > critch:
                        enemyhp -= damage
                        if enemyhp > 0:
                            input(Fore.MAGENTA + 'Ты нанесла {0} урона. У {1} теперь {2} здоровья'.format(damage,
                                                                                                          enemyname,
                                                                                                          enemyhp))
                            getting()
                    elif critreal <= critch:
                        input(Fore.BLUE + 'Ты собралась силами и нанесла мощный удар. Урон удвоен.')
                        enemyhp -= damage * 2

                        if enemyhp > 0:
                            input(Fore.MAGENTA + 'Ты нанесла {0} урона. У {1} теперь {2} здоровья'.format(damage * 2,
                                                                                                   enemyname,
                                                                                                        enemyhp))
                            getting()
                elif punchchance <= 10:
                    input(Fore.RED + 'Ты промазала...')
                    getting()
            elif actpl == '2':
                blockch = r.randint(1, 10)
                blockdmg = r.randint(1, 2)
                if blockch >= 3:
                    enemydamage = enemydamage / 2
                    input(Fore.CYAN + 'Ты поставила блок. Урон ' + enemyname + ' уменьшен вдвое на этот раз.')
                    if blockdmg == 1:
                        if enemyac >= 2:
                            getting()
                            enemyhp -= 1
                            input(
                                Fore.BLUE + 'Отразив атаку ' + enemyname + ' ты оттолкнула его нанеся 1 единицу урона.')
                            if enemyhp > 0:
                                input('У {0} теперь {1} жизней'.format(enemyname, enemyhp))
                                enemydamage = enemydamage * 2
                        elif enemyac == 1:
                            input(Fore.BLUE +'Вместо того чтобы ударить тебя '+enemyname+' с умным видом почесал нос. Зато ты заблокировал его во всех соцсетях.')
                            enemydamage = enemydamage * 2
                    else:
                        getting()
                        enemydamage = enemydamage * 2
                elif blockch < 3:
                    input(Fore.RED + 'Ты замешкалась и пропустила верный момент. Блок не удался.')
                    getting()
            elif actpl == '3':
                dodgech = r.randint(1, 10)
                if dodgech >= 5:
                    input(
                        Fore.RED + 'Ты сама не поняла обо что запнулась... Была ли это земля или своя же нога уже не важно...')
                    getting()
                elif dodgech <= 4:
                    dodge = 1
                    dodgedmg = r.randint(2, 3)
                    input(
                        Fore.CYAN + "Ты сосредоточилась и подловила " + enemyname + " на ошибке. Контратака удалась, ты нанесла {} урона".format(
                            dodgedmg))
                    enemyhp -= dodgedmg
                    input(Fore.MAGENTA + 'У {0} теперь {1} жизней'.format(enemyname, enemyhp))
            elif actpl == '4':
                leavech = r.randint(1, 100)
                if leavech >= 21:
                    input(Fore.RED + 'Попытка побега не удалась...')
                    getting()
                elif leavech <= 20:
                    input(
                        Fore.CYAN + "В отчаянии ты спряталась за одно из деревьев, надеясь что " + enemyname + " тебя не заметит.")
                    input("Тебе повезло, так и случилось")
                    fightisgoing = False
                    gameproc()
            elif actpl == '5' and len(inventory)>=1:
                showinv()
                fighthealing = 1
                healing()
                getting()
            else:
                print(Fore.RED + 'Выбери одно из действий')
        else:
            fightisgoing = False
            input(Fore.MAGENTA + 'Ты убила ' + enemyname)
            input(Fore.YELLOW + 'Неплохо, ты заслуживаешь награды в {0} монет'.format(loot))
            money += loot
            showwin()
            enemycounter += 1
            gameproc()
    else:
        gameproc()


def healing():
    global health, inventory, fighthealing
    healing = 1

    healfrombackpack = '-Выбери зелье для лечения, либо не смотри в меня'
    fightheal = '-Лечись скорее! Я не хочу чтобы мои швы разошлись!'
    healnopotinos ='-Не смотри в меня, тут ничего нет'

    if fighthealing == 1:
        healdesc = fightheal
    elif len(inventory) < 1:
        healdesc = healnopotinos
    else:
        healdesc = healfrombackpack


    while healing == 1:
        pemzele = input(Fore.WHITE+healdesc+' \n')
        if pemzele == '1' and len(inventory) >= 1:
            print(Fore.YELLOW + 'Ты излечился на {0} жизней'.format(inventory[0].value1))
            health += inventory[0].value1
            inventory.pop(0)
            showhp()
            if fighthealing == 1:
                healing = 0
                fighthealing = 0
            if healing == 1:
                showinv()
        elif pemzele == '2' and len(inventory) >= 2:
            print(Fore.YELLOW + 'Ты излечился на {} жизней'.format(inventory[1].value1))
            health += inventory[1].value1
            inventory.pop(1)
            showhp()
            if fighthealing == 1:
                healing = 0
                fighthealing = 0
            if healing == 1:
                showinv()
        elif pemzele == '3' and len(inventory) >= 3:
            print(Fore.YELLOW + 'Ты излечился на {} жизней'.format(inventory[2].value1))
            health += inventory[2].value1
            inventory.pop(2)
            showhp()
            if fighthealing == 1:
                healing = 0
                fighthealing = 0
            if healing == 1:
                showinv()
        elif pemzele == '4' and len(inventory) == 4:
            print(Fore.YELLOW + 'Ты излечился на {} жизней'.format(inventory[3].value1))
            health += inventory[3].value1
            inventory.pop(3)
            showhp()
            if fighthealing == 1:
                healing = 0
                fighthealing = 0
            if healing == 1:
                showinv()
        elif pemzele == str(len(inventory) + 1):
            healing = 0
            pass
        else:
            print(Fore.RED + 'Выбери число из списка')
            showinv()
    else:
        pass


def meetcity():
    global health
    global money
    global playerbet
    global map
    global enemycounter
    global ctticket
    global mapcost
    while health > 0:
        print(Fore.GREEN + 'Ты в городе, куда пойдёшь?')
        print(Fore.CYAN + "1) Зайти в городской магазин")
        print("2) Пойти заработать на ставках")
        print("3) Зайти к картографу")
        print("4) Выйти из города")
        ctch = input(Fore.BLUE + "")
        if ctch == '1':
            meetctshop()
        elif ctch == '2':
            input('Ты подошла к крупному зданию в центре города. Вывеска гласила "Кулачные бои".')
            input('Зайдя внутрь, ты увидела как двое мужиков набивали друг другу морды.')
            if input(
                    'К тебе подошёл работник заведения и спросил' + Fore.WHITE + '\n-Мисс, желаете сделать ставку? ').lower() == 'да':
                showmoney()
                while health > 0:
                    try:
                        betos = input(Fore.GREEN + 'Укажите размер ставки: ')
                        if int(betos) >= 0:
                            if money >= int(betos):
                                bet = int(betos)
                                winner = r.randint(1, 5)
                                money -= bet
                                winbet = 3 * bet
                                showmoney()
                                print(Fore.BLUE + 'Бойцы для ставок:')
                                print(Fore.CYAN + '1) Меннам - мускулистый лысый мужик с чёрной бородой')
                                print('2) Сьюза - стройная девушка, несущая меч в ножнах за спиной')
                                print('3) Хнекрог - молодой огр, имевший рост выше 2 метров')
                                print('4) Зиннель - эльф-полукровка с белыми волосами и безжизненным взглядом')
                                print('5) Неясная личность в плаще, выпивающая уже второй стакан эля на твоих глазах')
                                while health > 0:
                                    try:
                                        playerbet = input(
                                            Fore.WHITE + '-На какого бойца вы хотите сделать ставку, мисс? ')
                                        if int(playerbet) >= 1 and int(playerbet) <= 5:
                                            if winner == int(playerbet):
                                                input(
                                                    Fore.BLUE + 'Спустя пару минут, на ринг вышел твой боец и его соперник')
                                                money += winbet
                                                input('Твой боец наносит пару ошеломляющих ударов по противнику.')
                                                input(
                                                    'Спустя еще пару добрых ударов соперник пошатнулся и упал на пол.')
                                                input(
                                                    "Зал кричит. Кто-то восхваляет победителя, иные освистывают упавшего заживо...")
                                                input('К тебе подошёл работник, с которым ты говорила недавно')
                                                input(Fore.WHITE + '-Мисс, вот ваша награда в {0} монет'.format(winbet))
                                                showmoney()
                                                if input(
                                                        Fore.WHITE + '-Желаете сделать еще одну ставку, мисс?').lower() == 'да':
                                                    input('-Итак, сколько поставите, мисс?')
                                                else:
                                                    input('-Хорошего дня, мисс')
                                                    meetcity()
                                            else:
                                                input(
                                                    Fore.BLUE + 'Спустя пару минут, на ринг вышел твой боец и его соперник')
                                                input(
                                                    'Сначала все шло неплохо, твой боец выглядел устойчивее своего соперника')
                                                input('Ты уже подумала, что победа у тебя в кармане')
                                                input(
                                                    'Вдруг к тебе подошла эльфийка затмившая обзор арены, было ясно, что она заигрывает с тобой')
                                                input('Вдруг ты услышала глухой и громкий удар')
                                                input('Отдвинув эльфийку, ты увидела, что твой боец лежал на арене')
                                                input('К тебе подошёл работник, с которым ты говорил недавно')
                                                input(Fore.WHITE + '-Мисс, мне жаль, но вы проиграли...')
                                                if input('-Желаете сделать еще одну ставку, мисс?').lower() == 'да':
                                                    input('-Итак, сколько поставите, мисс?')
                                                else:
                                                    input('-Хорошего дня, мисс')
                                                    meetcity()
                                        else:
                                            input(Fore.RED + 'Введи цифру от 1 до 5')
                                    except ValueError:
                                        input(Fore.RED + 'Введи цифру от 1 до 5')
                            else:
                                input(Fore.RED + 'У тебя нет столько монет, введи сумму поменьше')
                        else:
                            input(Fore.RED + 'Введи положительное число')
                    except ValueError:
                        input(Fore.RED + 'Введи положительное число')
            else:
                input("-Тогда Вам нечего здесь делать.")
                meetcity()
        elif ctch == '3':
            meetmapper()
        elif ctch == '4':
            gameproc()


def meetmapper():
    global map
    global money
    global meetmap
    global mapcost
    if meetmap == 0:
        mapcost = 1000
        input(Fore.BLUE + 'Ты зашёл в здание с оригинальным названием: "Дом картографа"')
        input('За прилавком ты увидел старого гнома')
        if input(Fore.WHITE + '-Эй, ты, карту местности купить не хочешь?').lower() == 'да':
            input('-Хехе, эт хорошо, 1000 чеканных и она твоя')
            if input(Fore.GREEN + 'Попытаться сбить цену?').lower() == 'да':
                input(Fore.BLUE + 'Ты говоришь гному, что хочешь сторговаться')
                input(Fore.WHITE + '-Чёё? Сторговаться? Да ты хоть знаешь сколько я рисовал её?')
                if input(Fore.GREEN + 'Хочешь предложить свою цену?').lower() == 'да':
                    yourcost = input(Fore.GREEN + 'Какую сумму предложишь?')
                    try:
                        if int(yourcost) >= 0:
                            if int(yourcost) >= 501:
                                input(
                                    Fore.WHITE + '-Ох, совсем ты мою работу не ценишь... Но деньги мне нужны, по рукам')
                                mapcost = int(yourcost)
                                input(Fore.WHITE + '-Злато вперёд')
                                if money >= mapcost:
                                    money -= mapcost
                                    input(Fore.BLUE + 'Ты протянула огромный кошель монет')
                                    input(Fore.WHITE + '-Хехе, неплохо-неплохо, вот твоя карта')
                                    map = 1
                                    gameproc()
                                else:
                                    input(
                                        Fore.BLUE + 'Ты понимаешь, что у тебя нет денег на карту даже со скидкой')
                                    input(
                                        Fore.WHITE + '-Чё? Ты сторговалась со мной и у тебя всё равно не хватает? Какой тогда в этом смысл?')
                                    input('-Кхх, чёрт с тобой приходи как скопишь сумму')
                                    meetmap = 1
                                    meetcity()
                            else:
                                input(Fore.WHITE + '-Слышь, а ты не охренела?')
                                input('-Ну ка проваливай отсюда')
                                meetmap = 2
                                meetcity()
                        else:
                            input(Fore.RED + 'Введи положительное число')
                    except ValueError:
                        input(Fore.RED + 'Введи целое число')
                else:
                    input(Fore.WHITE + '-Эх, впрочем ладно, красавице могу сделать и скидку в 250 монет')

                    torg1 = input(
                        Fore.GREEN + 'Согласиться на скидку или торговаться еще?(согласиться\торговаться)')
                    if torg1.lower() == 'согласиться':
                        mapcost = 750
                        if money >= mapcost:
                            money -= mapcost
                            input('-Злато вперёд')
                            input(Fore.BLUE + 'Ты протянула огромный кошель монет')
                            input(Fore.WHITE + '-Хехе, неплохо-неплохо, вот твоя карта')
                            map = 1
                            meetcity()
                        else:
                            input(Fore.WHITE + '-Злато вперёд')
                            input(Fore.BLUE + 'Ты понимаешь, что у тебя нет денег на карту даже со скидкой')
                            input(
                                Fore.WHITE + '-Чё? Ты сторговалась со мной и у тебя всё равно не хватает? Какой тогда в этом смысл?')
                            input('-Кхх, чёрт с тобой приходи как скопишь сумму')
                            meetmap = 1
                            meetcity()
                    if torg1.lower() == 'торговаться':
                        torg2 = input(
                            Fore.WHITE + '-Нахалка, ну хорошо, я готов скинуть 400 монет со стоимости, по рукам?(согласиться\торговаться)')
                        if torg2.lower() == 'согласиться':
                            mapcost = 600
                            if money >= mapcost:
                                money -= mapcost
                                input('-Злато вперёд')
                                input(Fore.BLUE + 'Ты протянула огромный кошель монет')
                                input(Fore.WHITE + '-Хехе, неплохо-неплохо, вот твоя карта')
                                map = 1
                                meetcity()
                            else:
                                input(Fore.WHITE + '-Злато вперёд')
                                input(
                                    Fore.BLUE + 'Ты понимаешь, что у тебя нет денег на карту даже со скидкой')
                                input(
                                    Fore.WHITE + '-Чё? Ты сторговалась со мной и у тебя всё равно не хватает? Какой тогда в этом смысл?')
                                input('-Кхх, чёрт с тобой приходи как скопишь сумму')
                                meetmap = 1
                                meetcity()
                        if torg2.lower() == 'торговаться':
                            input(Fore.WHITE + '-Слышь, а ты не охренела?')
                            input('-Ну ка проваливай отсюда')
                            meetmap = 2
                            meetcity()
                        else:
                            input(Fore.RED + 'Введи один из вариантов ответа')
                    else:
                        input(Fore.RED + 'Введи один из вариантов ответа')
            else:
                if money >= mapcost:
                    money -= mapcost
                    input('-Злато вперёд')
                    input(Fore.BLUE + 'Ты протянула огромный кошель монет')
                    input(Fore.WHITE + '-Хехе, неплохо-неплохо, вот твоя карта')
                    map = 1
                    gameproc()
                else:
                    input(Fore.WHITE + '-Злато вперёд')
                    input(Fore.BLUE + 'Ты понимаешь, что у тебя нет денег на карту')
                    input(
                        Fore.WHITE + '-Чё? Нет столько? Кхх, и зачем тогда согласилась покупать?')
                    input('-Кхх, чёрт с тобой приходи как скопишь сумму')
                    meetcity()
        else:
            input(Fore.WHITE + '-Ну и проваливай тогда')
            meetcity()
    elif meetmap == 1:
        input(Fore.WHITE + '-Охохо, какая гостья!')
        input('-Ну что, принесла как и договаривались?')
        if money >= mapcost:
            input(Fore.BLUE + 'Ты протянула огромный кошель монет')
            input(Fore.WHITE + '-Хехе, неплохо-неплохо, вот твоя карта')
            map = 1
            gameproc()
        else:
            input(Fore.BLUE + 'Ты не уверено покачала головй из стороны в сторону')
            input(Fore.WHITE + '-Нет? Так чего ты ждешь?')
            meetcity()
    elif meetmap == 2:
        input(Fore.WHITE + '-Опять ты пришла, нахалка?')
        input('-Если нет 1000, то проваливай')
        if money >= 1000:
            input(Fore.BLUE + 'Ты робко протягиваешь 2 больших мешочка с золотом')
            input(Fore.WHITE + '-Ну надо же, какая ты щедрая')
            input('-Чёрт с тобой, бери свою карту и проваливай из моего магазина')
            input(Fore.BLUE + 'Гном протянул тебе карту, и ты осторожно её взяла, а после вышла из магазина')
            map = 1
            gameproc()
        else:
            input(Fore.WHITE + '-И на кой чёрт ты тогда пришла сюда?')
            meetcity()


def meetshop():
    global health, money, damage, critch, armor, inventory, meetshop1, maptoct
    meetshop1 = 1
    standinshop = True



    armor1=Armor()
    armor1.genercommonmerch()
    weapon1=Weapon()
    weapon2=Weapon()
    weapon1.gener()
    weapon2.gener()
    healthpotions1 = Potion()
    healthpotions1.gener()

    input(Fore.BLUE + "Ты увидела горбатого старичка, он предложил тебе посмотреть его товары")
    showmoney()
    if input(Fore.GREEN + 'Взглянуть на товары? ').lower() == 'да':
        while standinshop:

            print(Fore.CYAN + "1) Уйти")
            print("2) Зелья здоровья " + str(healthpotions1.lvl) + " уровня - " + str(healthpotions1.cost) + ' монет')
            print("3) {0} - {1} урона и {2}% шанса крита - {3} монет".format(weapon1.name,weapon1.damage,weapon1.crit,weapon1.cost))
            print('4) {0} - {1} урона и {2}% шанса крита - {3} монет'.format(weapon2.name,weapon2.damage,weapon2.crit,weapon2.cost))
            print('5) {0}. Имеет {1} брони - {2} монет'.format(armor1.name, armor1.armor, armor1.cost))
            print("6) Карта местности - 100 монет")


            choise = input(Fore.GREEN + "Что хочешь приобрести? ")



            if choise == "1":
                standinshop = False
                gameproc()
            elif choise == "2":
                if len(inventory) < 4:
                    if buy(healthpotions1.cost):
                        inventory.append(healthpotions1)
                        input(Fore.BLUE+(healthpotions1.name+' '+str(healthpotions1.lvl)+' уровня теперь в твоем рюкзаке'))
                else:
                    print('В твоем рюкзаке недостаточно места')
                    if input(Fore.GREEN+'Хочешь купить зелье и излечитсья сразу?').lower() == 'да':
                        if buy(healthpotions1.cost):
                            healing = healthpotions1.value1
                            health += healing
                            print(Fore.YELLOW + 'Ты излечился на {0}'.format(healing))
                            showhp()
            elif choise == '3':
                if buy(weapon1.cost):
                    damage = weapon1.damage
                    critch = weapon1.crit
                    showdmg()
            elif choise == '4':
                if weapon2.isbought == 1:
                    print(Fore.WHITE + '-Ты ведь его уже купила')
                elif buy(weapon2.cost) and weapon2.isbought==0:
                    damage = weapon2.damage
                    critch = weapon2.crit
                    weapon2.isbought = 1
                    showdmg()

            elif choise == "5":
                if buy(armor1.cost):
                    armor = armor1.armor
                    showarm()
            elif choise == "6":
                if buy(100):
                    maptoct = 1
                    input(Fore.WHITE+'-Хехехе, не теряй эту карту, путник')

            else:
                print(Fore.RED + "ты помоему перепутал")
    else:
        gameproc()


def meettrollshop():
    global health
    global money
    global damage
    global critch
    global map
    standinshop = True
    weapon1=Weapon()
    weapon1.genertrollmerch()
    if input('Взглянуть на товары? ').lower() == 'да':
        while standinshop:
            print(Fore.CYAN + "1) Кусочек бумаги в соплях троля - 300 монет ")
            print(
                "2) {0}. Имеет {1} урона и {2}% шанса крита- {3} монет".format(weapon1.name,weapon1.damage,weapon1.crit,weapon1.cost))
            print("3) Уйти")
            choise = input(Fore.GREEN + "Что хочешь приобрести? ")
            if choise == "1":
                if buy(300):
                    map = 1
                    input(Fore.WHITE + '-Ты серьёзно купила у меня эту бумажку за такую цену?' +
                          '\n-Да ты сама богиня щедрости, спасибо тебе')
                    input(Fore.BLUE + 'Троль ехидно улыбнулся и убежал так быстро, как только вобще мог')
                    input('Приложив свою кофту к бумаге, чтобы впитать лишнюю влагу, ты поняла, что это была карта')
                    gameproc()
            elif choise == '2':
                if buy(weapon1.cost):
                    damage = weapon1.damage
                    critch = weapon1.crit
                    showdmg()
            elif choise == "3":
                standinshop = False
                gameproc()
            else:
                print(Fore.RED + "ты помоему перепутал")
    else:
        gameproc()


def meetctshop():
    global health, armor
    global money
    global damage
    global critch
    standinshop = True

    armor1=Armor()
    armor1.generctmerch()
    weapon1 = Weapon ()
    weapon2 = Weapon ()
    weapon1.generctmerch()
    weapon2.generctmerch()
    healthpotion = Potion()
    healthpotion.generctmerch()

    print(Fore.BLUE + "Ты зашла в главный магазин города")
    showmoney()

    while standinshop:
        print(Fore.CYAN + "1) Зелья здоровья " + str(healthpotion.lvl) + " уровня - " + str(
            healthpotion.cost) + ' монет')
        print("2) {0}. Имеет {1} урона и {2}% шанса крита - {3} монет".format(weapon1.name, weapon1.damage,weapon1.crit,weapon1.cost))
        print("3) {0}. Имеет {1} урона и {2}% шанса крита - {3} монет".format(weapon2.name, weapon2.damage,weapon2.crit,weapon2.cost))
        print('4) {0}. Имеет {1} брони - {2} монет'.format(armor1.name,armor1.armor,armor1.cost))
        print("5) Уйти")
        choise = input(Fore.GREEN + "Что хочешь приобрести? ")
        if choise == "1":
            if len(inventory) < 4:
                if buy(healthpotion.cost):

                    inventory.append(healthpotion)
            else:
                print('В твоем рюкзаке недостаточно места')
                if input(Fore.GREEN+'Хочешь купить зелье и излечитсья сразу?').lower() == 'да':
                    if buy(healthpotion.cost):
                        healing = healthpotion.lvl + r.randint(2, 3)
                        health += healing
                        print(Fore.YELLOW + 'Ты излечился на {0}'.format(healing))
                        showhp()
        elif choise == '2':
            if buy(weapon1.cost):
                damage = weapon1.damage
                critch = weapon1.crit
                showdmg()
        elif choise == '3':
            if buy(weapon2.cost):
                damage = weapon2.damage
                critch = weapon2.crit
                showdmg()
        elif choise == "4":
            if buy(armor1.cost):
                armor = armor1.armor
                showarm()
        elif choise == "5":
            standinshop = False
            meetcity()
        else:
            print(Fore.RED + "ты помоему перепутал")


def meetfight():
    global health
    global money
    global damage
    global enemyname
    global enemylvl
    global enemylvldefined
    global keygirl
    enemynames = ["Бродяга-вор", "Ученик-волшебник", "Одичавший енот-переросток", "Обзеумевший стражник", "КОЙОТ",
                  "Наёмный убийца", "Молодой дракон", "Гном-недорослик", "Эльф-полукровка", "Птица-мутант",
                  "Чародейка-самоучка", "Старый рыцарь", "Гоблин"]
    enemyname = r.choice(enemynames)

    meetdesc1 = Fore.BLUE + 'Тебе встретилась загадочная личность в черном плаще, он предлагет тебе работенку'
    meetdesc2 = Fore.BLUE + 'Гуляя по бездушному лесу ты услышал крик девочки'
    meetdesc3 = Fore.BLUE + 'На тебя выбежало что-то и резко толкнуло, ты не успела опомниться как в тебя прилетел уже новый удар'
    meetdesc4 = Fore.BLUE + 'Гуляя по лесу ты услышала голоса левее тебя'
    meetdesc5 = Fore.BLUE + 'Ты встретила сундук посредине поляны, рядом была табличка с надписью: "Впереди - мимик"'
    meetdesc6 = Fore.BLUE + 'Ты встретила сундук посредине поляны, рядом была табличка с надписью: "Впереди - не мимик"'
    meetdesc7 = Fore.BLUE + 'Тебе стало скучно и ты решила кого-нибудь ограбить'
    meetdesc8 = Fore.BLUE + 'Тебе стало жарко и ты решил прилечь под дерево чтобы остудиться'

    meetdescvar = [meetdesc1, meetdesc2, meetdesc3, meetdesc4, meetdesc5, meetdesc6, meetdesc7, meetdesc8]
    meettype = r.choice(meetdescvar)
    input(meettype)
    if meettype == meetdesc1:
        if input(Fore.GREEN + 'Согласишься?').lower() == "да":
            while health > 0:
                input(Fore.GREEN + 'Он заказал убить кое-кого. Дав наводку и кинув деньги он ушёл')
                input('На земле валяется увесистый мешочек')
                dard1 = input(Fore.GREEN + 'Выполнишь заказ или сбежишь с деньгами? (выполнить\сбежать)')
                if dard1.lower() == "выполнить":
                    input('Взяв мешочек ты пересчитала деньги. В нем было 50 монет')
                    money += 50
                    print("Спустя 2 часа поисков ты нашел того кто был указан в наводке")
                    fight()
                elif dard1.lower() == "сбежать":
                    input('Ты взяла мешочек с ухмылкой и быстро побрела дальше')
                    money = money + r.randint(40, 55)
                    showmoney()
                    input("Заказчик не одобрил таких мемов и решил побить тебя бесплатно")
                    enemyname = 'Заказчик'
                    enemylvl = r.randint(2, 4)
                    enemylvldefined = 1
                    fight()
                else:
                    input(Fore.RED + 'Выбери одно из действий')
        else:
            gameproc()
    if meettype == meetdesc2:
        if input(Fore.GREEN + 'Побежать на крики?').lower() == "да":
            fight()
            print(Fore.BLUE+'Девочки и след простыл...')
            keygirl = 1
        else:
            gameproc()
    if meettype == meetdesc3:
        input(Fore.GREEN + 'Тебе остается сражаться...')
        fight()
    if meettype == meetdesc4:
        if input(Fore.GREEN + 'Хочешь подойди и подслушать?').lower() == "да":
            print("Ты не особо отличалась скрытностью и тебя сразу же заметили бандиты, обсуждающие свой план...")
            fight()
        else:
            gameproc()
    if meettype == meetdesc5:
        if input(Fore.GREEN + 'Подойти к сундуку?').lower() == "да":
            input(Fore.BLUE + 'Как только ты притронулась к сундуку, ты услышала чих')
            input(Fore.WHITE + ('-Даже не скажешь "будь здоров"?'))
            input('-Как грубо...')
            enemyname = "Грустный мимик"
            fight()
        else:
            print(Fore.BLUE + 'Сундук расстроился, что ты не хочешь подходить к нему, поэтому он сам подошел к тебе...')
            enemyname = "Грустный мимик"
            fight()
    if meettype == meetdesc6:
        if input(Fore.GREEN + 'Подойти к сундуку?').lower() == "да":
            input(Fore.BLUE + 'Как только ты притронулась у сундуку, ты услышала чих')
            input(Fore.WHITE + ('-Даже не скажешь "будь здоров"?'))
            input('-Как грубо...')
            enemyname = "Грустный мимик"
            fight()
        else:
            gameproc()
    if meettype == meetdesc7:
        enemylvl = 5
        for i in range (0,10):
            if i == 9:
                enemylvldefined = 0
                input(Fore.BLUE+'Тебе надоело искать жертву и ты пошла дальше по своим четным неворовским делам...')
                waychoise()
            else:
                enemylvldefined = 1
                print(Fore.GREEN + "Тебе попался {0} {1} уровня".format(enemyname, enemylvl))
                if input(Fore.GREEN + 'Махаца буш? ').lower() == "да":
                    fight()
                else:
                    enemyname = r.choice(enemynames)
                    enemylvl = r.randint(1, 5)


    if meettype == meetdesc8:
        input("Дерево такова мема не поняло и решило тебя прогнать")
        enemyname = "Афигевшее от твоей наглости дерево"
        fight()


def meettreasure(mvtype):
    global money
    global health
    global map
    global enemyname
    global enemylvl
    global enemylvldefined
    global damage
    global keygirl
    global ctticket
    global critch,mvinit,mvvars

    mvvars = [mv1, mv2, mv3, mv4, mv5, mv6, mv7, mv8, mv9, mv10, mv11, mv12, mv13, mv14, mv16, mv17, mv18, mv19, mv20]

    if mvtype == 0:
        mvtype = r.choice(mvvars)
    else:
        pass

    input(mvtype)
    if mvtype == mv1:
        if input(Fore.GREEN +
                 'Есть риск быть обкраденным, но может стоит передохнуть?(передохнуть\уйти)').lower() == "передохнуть":
            mv1ch = r.randint(1, 100)
            if mv1ch == 1:
                input(Fore.RED + 'Тебе перерезали глотку во сне...')
                health = 0
            elif mv1ch >= 2 and mv1ch <= 16:
                input(Fore.BLUE + 'Проснувшись, ты поняла, что тебя обокрали... Зато выспалась')
                money = 0
                health = health + r.randint(1, 3)
                showwin()
                gameproc()
            elif mv1ch >= 17:
                input(Fore.BLUE + 'Ты спокойно поспала и восстановила силы')
                health = health + r.randint(1, 2)
                showwin()
                gameproc()
            else:
                input(Fore.RED + 'Пиши внимательней')
        else:
            gameproc()
    if mvtype == mv2:
        input('Ты споткнулась и упала прямо на ежа... Ежа жалко...')
        health = health - 1
        input('Ты потеряла 1 жизнь.')
        if health < -0:
            input(Fore.RED + 'Какая нелепая смерть...')
            gameproc()
        showhp()
        gameproc()
    if mvtype == mv3:
        if input(Fore.GREEN + 'Подойти к сундуку?').lower() == "да":
            input("Ты подошла к сундуку и открыла его")
            tr1 = r.randint(1, 100)
            if tr1 == 1:
                input("Ты нашла карту местности")
                map = 1
            if tr1 >= 2:
                moneychest = r.randint(40, 80)
                input('Ты нашла {} монет'.format(moneychest))
                money = money + moneychest
                showmoney()
                gameproc()
        else:
            gameproc()
    if mvtype == mv4:
        if input(Fore.GREEN + 'Подойти к сундуку?').lower() == "да":
            input("Ты подошла к сундуку и открыла его")
            tr1 = r.randint(1, 100)
            if tr1 == 1:
                input("Ты нашла карту местности")
                map = 1
            if tr1 >= 2:
                moneychest = r.randint(1, 40)
                input('Ты нашла {} монет'.format(moneychest))
                money = money + moneychest
                showmoney()
                gameproc()
        else:
            gameproc()
    if mvtype == mv5:
        print('Что же будешь делать?')
        print(Fore.CYAN + "1) Пойти назад ")
        print("2) Сидеть и ждать...")
        print('3) Крикнуть "Кто здесь?"')
        choise = input()
        if choise == str(1):
            input(Fore.GREEN + 'Спустя время ты поняла что все стало на свои места')
            gameproc()
        elif choise == str(2):
            input(Fore.GREEN + 'Спустя 2 часа ожидайний ты встала и пошла')
            gameproc()
        elif choise == str(3):
            input(Fore.GREEN + 'Ты крикнула. Никто не отвтеил. Ты пошла дальше.')
            gameproc()
        else:
            input(Fore.RED + 'Пиши внимательней')
    if mvtype == mv6:
        if input(Fore.GREEN + 'Проследовать за ней?').lower() == "да":
            input(Fore.BLUE + 'Следуя за девушкой ты прошел минут 20, как вдруг она остановилась посреди озера.')
            if input(Fore.GREEN + 'Нырнуть в озеро?').lower() == "да":
                if input(
                        "Нырнув ты увидел в самой глубине меч, воздуха и так немного, погружаться глубже?").lower() == "да":
                    lakesworddamage = r.randint(3, 4)
                    lakeswordcrit = r.randint(30, 40)
                    input(Fore.BLUE + 'Ты достал меч и быстро всплыл вверх')
                    input('Твоим лёгким это не понравилось')
                    damage = lakesworddamage
                    critch = lakeswordcrit
                    lakelose = r.randint(3, 5)
                    if lakelose >= health:
                        lakelose = health - 1
                    health = health - lakelose
                    input('Теперь у тебя {0} урона и {1}% шанса крита, но ты потеряла {2} жизней.'.format(damage,
                                                                                                          lakeswordcrit,
                                                                                                          lakelose))
                    showhp()
                    gameproc()
                else:
                    input(Fore.BLUE + 'Ты быстро всплыла и досадно побрела дальше.')
                    gameproc()
            else:
                input(Fore.BLUE + 'Обидевшись, что ты потеряла столько времени ты просто ушла.')
                gameproc()
        else:
            gameproc()
    if mvtype == mv7:
        if input(Fore.GREEN + 'Хочешь подойти помочь?').lower() == "да":
            input(Fore.BLUE + 'Как только ты подошла ближе девшка превратилась в обортня')
            enemyname = "Женщина-оборотень"
            fight()
        else:
            gameproc()
    if mvtype == mv8:
        if input(Fore.GREEN + 'Пойти по следам?').lower() == ("да"):
            input(Fore.BLUE + "Спустя пару сотен метров ты натыкаешься на жирного троля ростом не менее 6 метров")
            trollchoise = input(Fore.GREEN + 'Он явно спит, хочешь его разбудить?')
            if trollchoise.lower() == "да":
                troalagr = r.randint(1, 3)
                if troalagr == 1:
                    input(Fore.BLUE + "Ты разбудила троля.")
                    input('Он вежливо тебя приветствует и предлагает посмотреть его товары на продажу')
                    showmoney()
                    meettrollshop()
                if troalagr > 1:
                    trolevdam = r.randint(1, 3)
                    health -= trolevdam
                    input(
                        Fore.BLUE + 'Ты разбудила троля. Он резко вскочил и оттолкнул тебя на десяток метров. Было больно' +
                        '\nТы потеряла {0} жизни'.format(trolevdam))
                    if health <= 0:
                        input(Fore.RED + 'Похоже этот толчок стал для тебя смертельным...')
                        gameproc()
                    enemyname = "Огромный троль"
                    enemylvl = r.randint(5,7)
                    enemylvldefined = 1
                    fight()
            else:
                gameproc()
        else:
            gameproc()
    if mvtype == mv9:
        if input(Fore.GREEN + 'Хочешь рассмотреть поближе листовку? ').lower() == "да":
            input(
                Fore.BLUE + "Подойдя ближе, ты прочла: 'Здраствуйте " + username + ", чтобы встать на учет в ученики магов вам нужно прочесть заклинание.'")
            input("'Звучит оно так - Феногельс днукусо' ")
            if input(Fore.GREEN + "Произнеси заклинание: ").lower() == 'феногельс днукусо':
                input(Fore.BLUE + 'Надпись на листовке изменилась и теперь выглядит так:')
                input('Поздравляем ' + username + ', вы встали на учет учеников магов. Мы перезвоним вам позже.')
                gameproc()
            else:
                input(
                    Fore.BLUE + 'Листовка моментально сгорела в пепел. Видимо ты неправильно произнесла заклинание...')
                gameproc()
        else:
            gameproc()
    if mvtype == mv10:
        while health > 0:
            if input(
                    Fore.GREEN + 'Есть риск быть обкраденным, но может стоит передохнуть?(передохнуть\уйти)').lower() == "передохнуть":
                mv1ch = r.randint(1, 100)
                if mv1ch == 1:
                    input(Fore.RED + 'Тебе перерезали глотку во сне...')
                    health = 0
                elif mv1ch >= 2 and mv1ch <= 16:
                    input(Fore.BLUE + 'Проснувшись, ты поняла, что тебя обокрали... Зато выспалась')
                    money = 0
                    health = health + r.randint(1, 3)
                    showwin()
                    gameproc()
                elif mv1ch >= 17:
                    input(Fore.BLUE + 'Ты спокойно поспала и восстановила силы')
                    health = health + r.randint(2, 3)
                    showhp()
                    gameproc()
                else:
                    input(Fore.RED + 'Пиши внимательней')
            else:
                gameproc()
    if mvtype == mv11:
        if input(Fore.GREEN + 'Зайти в лачугу?').lower() == 'да':
            input(Fore.BLUE + 'Ты зашла внутрь. Здесь очень тихо и темно.')
            if input(Fore.GREEN + 'Поискать полезности?').lower() == 'да':
                lachch = r.randint(1, 2)
                if lachch == 1:
                    input(Fore.BLUE + 'Ты нашла фруктов на перекус и решила уйти из этого жуткого строения')
                    health = health + 3
                    showhp()
                    gameproc()
                if lachch == 2:
                    enemyname = 'Шкафный червь'
                    enemylvl = r.randint(1, 2)
                    enemylvldefined = 1
                    input(Fore.BLUE + 'Открыв один из ящиков на тебя упало нечто слизкое...')
                    fight()
            else:
                input(Fore.BLUE + 'Постояв в тишине пару минут, ты решил уйти')
                gameproc()
        else:
            gameproc()
    if mvtype == mv12:
        if input(Fore.GREEN + 'Хочешь зайти на территорию деревни?').lower() == "да":
            input(Fore.BLUE + 'Ты зашла в деревню. Здесь действительно очень пусто, лишь стоят дома.')
            if input(Fore.GREEN + 'Хочешь заглянуть в один из домов?').lower() == 'да':
                input(Fore.BLUE + 'Ты зашла в один из домов. В нем ничего не было.')
                input('Это просто пустая деревня, что ты ожидала здесь увидеть?')
                gameproc()
            else:
                gameproc()
        else:
            gameproc()
    if mvtype == mv13:
        if input(Fore.GREEN + "Хочешь пойти на запах?").lower() == "да":
            input(Fore.BLUE + 'Ты пошла на запах.')
            input('Обойдя пару деревьев ты увидела перед собой костёр, на котором жарился огромный кусок мяса')
            while health > 0:
                meatev = input(Fore.GREEN + 'Рядом никого нет. Что будешь делать?(подождать\украсть)')
                if meatev == 'подождать':
                    input(Fore.BLUE + 'Спустя полчаса к костру подошёл человек в шкурах зверей.')
                    input('Увидев тебя он нисколько не удивился, лишь предложил тебе кусочек жареного мяса')
                    if input(Fore.GREEN + 'Примешь его подарок?').lower() == 'да':
                        input(Fore.BLUE + 'Ты согласилась на его дар.')
                        input('Ты съела этот кусочек и почувствовала себя намного лучше')
                        meatbuff = r.randint(1, 2)
                        damage = damage + meatbuff
                        meatcrit = r.randint(5, 10)
                        critch += meatcrit
                        input('Твой урон стал на {0} выше, а шанс крита увеличился на {1}%'.format(meatbuff, meatcrit))
                        input(
                            'Пока ты насыщалась мясом ты упустила как человек в шкуре пропал, и костер с мясом тоже...')
                        gameproc()
                    else:
                        input(Fore.BLUE + '"Неблагодарный" - сказал человек в шкурах и пропал на твоих глазах.')
                        gameproc()
                elif meatev == "украсть":
                    input(Fore.BLUE + 'Ты жадно набросилась на этот кусок сочного мяса.')
                    input('В эту же секунду появился человек в шубе.')
                    input('"Какой низкий поступок..." - сказал он - "Ты заслужила это проклятье".')
                    input('Ты резко почувствовала себя чертовски плохо')
                    meatcurse = r.randint(3, 5)
                    meatcurse2 = r.randint(1, 2)
                    if meatcurse > health:
                        meatcurse = health - 1
                    health -= meatcurse
                    if meatcurse2 > damage:
                        meatcurse = damage - 1
                    damage -= meatcurse2
                    input('Ты потеряла {0} жизней и {1} урона '.format(meatcurse, meatcurse2))
                    gameproc()
                else:
                    input(Fore.RED + "Ты написала что-то неверно")
        else:
            gameproc()
    if mvtype == mv14:
        dieornot = r.randint(1,8)
        input(Fore.BLUE + 'Присмотревшись на одну из веток деревьев, ты увидела бледный силуэт, целившийся в тебя из лука')
        while health > 0:
            print(Fore.GREEN + 'Ты понимаешь что у тебя мало времени для действий, что предпримешь?')
            print(Fore.CYAN + '1) Уворот влево')
            print('2) Уворот вправо')
            print('3) Упасть на землю вниз')
            print('4) Стоять на месте')

            playerchoise = input()
            try:                                                             #ПРОВЕРКА ДАННЫХ
                if int(playerchoise) > 4 or int(playerchoise) < 1:
                    input(Fore.RED + 'Выбери цифру из списка')
                else:                                                         #ДАННЫЕ ВЕРНЫЕ
                    if int(playerchoise) == 4 or dieornot == 8:
                        input(Fore.RED + 'Стрела прилетела прямо тебе в глаз.')
                        health = 0
                        gameproc()
                    else:
                        if dieornot>= 6 and dieornot <= 7:
                            input(
                                Fore.BLUE + "Стрела прилетела тебе прямо в колено, и ты уже было хотел заканчивать дорогу приключений")
                            input(Fore.RED + "Ты потеряла 1 жизнь")
                            health -= 1
                            if health > 0:
                                input(Fore.BLUE + "Но воля к жизни тебя останавила")
                                if int(playerchoise) == 1:
                                    input(
                                        Fore.BLUE + "Ты бросилась вперед лишь бы избежать очередного знакомства со стрелой ")
                                    meettreasure(mv15)

                                if int(playerchoise) == 2:
                                    input(
                                        Fore.BLUE + "Ты бросилась вперед лишь бы избежать очередного знакомства со стрелой ")
                                    meetshop()
                                if int(playerchoise) == 3:
                                    input(Fore.BLUE + "Ты понимаешь что лёжа ты стала легкой мишенью")
                                    input("Рядом с твоей рукой упала еще одна стрела")
                                    input("Похоже на то, что твой убийца не особо умелый стрелок")
                                    print("Что будешь делать дальше?")
                                    print(Fore.CYAN + '1) Попытаться начать нерпиужденный диалог криком в его сторону')
                                    print('2) Резко встать и попытаться убежать')
                                    print('3) Лежать на месте')
                                    archereventchoise = input()
                                    try:
                                        if int(archereventchoise) > 3 or int(archereventchoise) < 1:
                                            input(Fore.RED + 'Выбери цифру из списка')
                                        if int(archereventchoise) == 1:
                                            input(Fore.RED + "Как только ты пытаешься открыть рот для социального взаимодействия с личностью сомнительной социольности, тут же его затыкает стрела...")
                                            health = 0
                                            gameproc()

                                        if int(archereventchoise) == 2:
                                            input(Fore.BLUE + "Ты очень резко встала и запнулась об что-то живое.")
                                            input(Fore.BLUE + "Ежа жалко.")
                                            input(Fore.RED + "Ты потеряла 1 жизнь")
                                            health -= 1
                                            if health > 0:
                                                input(Fore.BLUE + "Но вспомниая про своего обидчика ты начинаешь бежать оттуда как можно скорее")
                                                gameproc()
                                            else:
                                                input(Fore.RED + "Какая нелепая смерть")
                                                gameproc()
                                        if int(archereventchoise) == 3:
                                            input(Fore.BLUE + "Рядом с тобой упала еще одна стрела")
                                            input(Fore.BLUE + "И еще одна")
                                            input(Fore.BLUE + "И еще")
                                            input(Fore.BLUE + "И еще...")
                                            input(Fore.BLUE + "И вот она летит снова!")
                                            input(Fore.BLUE + "Но на этот раз ты почти уверена, что без жертвы не обойтись")
                                            input(Fore.BLUE + "Буквально перед тобой пробегает случайный заяц, минуя тебя прыжком он ловит неприятный подарок")
                                            input(Fore.BLUE + "Заяц упал замертво, а из леса ты услышал чей-то жалкий вопль ")
                                            input(Fore.BLUE + "Ты пролежала еще пару минут и пошла дальше по своим делам")
                                            gameproc()

                                    except ValueError:
                                        input(Fore.RED + 'Выбери цифру из списка')
                            if health <= 0:
                                input(
                                    Fore.RED + "И на этом ты действительно закончил карьеру путешественника. Непреднамеренно.")
                                gameproc()
                        if dieornot <= 5:
                            input(Fore.BLUE + "Стрела пролетела прямо у твоего виска, но всё-таки не коснулась тебя")
                            input('Ты быстро поняла, что нужно бежать в чащу леса, и так и сделала')
                            gameproc()
            except ValueError:
                input(Fore.RED + 'Выбери цифру из списка')
    if mvtype == mv15:
        maptoct = 1
        if ctticket == 1:
            input(Fore.WHITE + '-О, да ты же та, с подозрительной мордой... Ну проходи-проходи')
            meetcity()

        input('Подойдя ближе ты видишь стражников.')
        input(Fore.WHITE + '-Стой, кто идёт?')
        input('-Не знаю кто ты, но морда у тебя подозрительная, я пропущу тебя в город только за 100 золотых.')
        if input(Fore.GREEN + 'Отдать стражнику 100 монет?').lower() == "да":
            if money >= 100:
                money -= 100
                ctticket = 1
                meetcity()
            else:
                input(Fore.WHITE + '-Да ведь у тебя денег то и нет, проваливай пока я не разозлился.')
                gameproc()
        else:
            gameproc()
    if mvtype == mv16:
        if input(Fore.GREEN + 'Подойти ближе?').lower() == 'да':
            input(Fore.BLUE + 'Ты видишь меню ввода пин кода.')
            while health > 0:
                if input(Fore.GREEN + 'Хочешь ввести код? ').lower() == "да":
                    code = input('Вводи пин код: ')
                    if code == str(937):
                        input(Fore.BLUE + 'Высветилось "Access allowed"')
                        input('Появилась меню со стрелочками')
                        while health > 0:
                            if input(Fore.GREEN + 'Хочешь ввести код со стрелочками?').lower() == 'да':
                                print(Fore.CYAN + '1) Влево')
                                print('2) Верх')
                                print('3) Вправо')
                                print('4) Вниз')
                                seccode = input(Fore.GREEN + 'Что ввести?')
                                if seccode == str(4231):
                                    input(Fore.BLUE + 'Высветилась надпись "Portal was activated"')
                                    input('Внезапно все потемнело, ты отключилась')
                                    input('Ты проснулась в своей кровати.')
                                    endgame()
                                else:
                                    input(Fore.BLUE + 'Высветилось "Incorrect password"')
                                    input('Меню с пин кодом погасло, тебе остаётся уйти...')
                                    gameproc()
                            else:
                                gameproc()
                    else:
                        input(Fore.BLUE + 'Высветилось "Incorrect password"')
                        input('Меню с пин кодом погасло, тебе остаётся уйти...')
                        gameproc()
                else:
                    gameproc()
        else:
            gameproc()
    if mvtype == mv17:
        if input(Fore.GREEN + 'Подойти ближе?').lower() == 'да':
            input(Fore.BLUE + 'Ты подошла ближе и надпись исчезла. Перед тобой вновь обычное дерево...')
            input('К чему бы это?')
            gameproc()
        else:
            gameproc()
    if mvtype == mv18:
        input('Тебе остаётся бежать со всех ног.')
        input('Пробежав 300 метров и получив с десяток укусов пчёл ты увидел реку')
        if input(Fore.GREEN + 'Прыгнуть в реку?').lower() == "да":
            input(Fore.BLUE + 'Окунувшись в воду ты уже думал, что все кончено...')
            input('Но вдруг ты понял, что река просто переполнена электрическими угрями.')
            input("Еще пара секунд и они подплывут познакомитсья с тобой.")
            while health > 0:
                kazus = input(Fore.GREEN + 'Какой план?(всплыть\остаться)')
                if kazus == 'всплыть':
                    input(Fore.BLUE + 'Ты всплыла и пчелы тут же накинулись на тебя вновь.')
                    input('Ты пробежала еще километра 3 пока пчёлы не кончились...')
                    input('Твоё тело переполнено пчелиным ядом')
                    health = 1
                    input(Fore.YELLOW + 'У тебя осталась 1 жизнь.')
                    gameproc()
                elif kazus == "остаться":
                    input(Fore.BLUE + 'Угри подплыли к тебе и начали обниматься')
                    input('Ты понимаешь, что им просто одиноко, поэтому не уплываешь, а просто терпишь эту боль...')
                    input('Всё же, спустя пару минут, ты начинаешь задыхаться и уже непроизвольно всплываешь')
                    input('Всплыв ты не увидел пчел, но твое тело было на пределе')
                    health = 1
                    input(Fore.YELLOW + 'У тебя осталась 1 жизнь.')
                    gameproc()
                else:
                    input(Fore.RED + 'Писать научись')
        else:
            input(Fore.BLUE + 'Не прыгнув по какой-то причине в воду, ты решил бежать куда глаза глядят')
            input('Ты пробежала еще километра 3 пока пчёлы не кончились...')
            input('Твоё тело переполнено пчелиным ядом')
            health = 1
            input(Fore.YELLOW + 'У тебя осталась 1 жизнь.')
            gameproc()
    if mvtype == mv19:
        input('Ты буквально падаешь, потому что ноги тебя не держат.')
        input('Проснувшись ты понимаешь что тебя обкрали...')
        money = 0
        showmoney()
        gameproc()
    if mvtype == mv20:
        while health > 0:
            keych = input(Fore.GREEN + 'Что ответишь?(да\нет)')
            if keych.lower() == 'да' and keygirl == 1:
                input(
                    Fore.WHITE + '-Внушай и запоминай, дитя: те кто падают - после поднимаются, а правые не ходят налево.')
                input(Fore.BLUE + 'Девочка исчезла.')
                input('К чему бы это?')
                gameproc()
            elif keych.lower() == 'нет' and keygirl == 1:
                input(Fore.WHITE + '-Жаль, что не помнишь меня... Но я раскрою всё-таки я раскрою тебе тайну.')
                input('-Внушай и запоминай, дитя: те кто падают - после поднимаются, а правые не ходят налево.')
                input(Fore.BLUE + 'Девочка исчезла.')
                input('К чему бы это?')
                gameproc()
            elif keych.lower() == 'да' and keygirl == 0:
                input(Fore.WHITE + '-Зачем ты обманываешь меня?')
                input(Fore.BLUE + 'Девочка исчезла.')
                gameproc()
            elif keych.lower() == 'нет' and keygirl == 0:
                input(Fore.WHITE + '-Значит мы еще встретимся...')
                input(Fore.BLUE + 'Девочка исчезла.')
                input('К чему бы это?')
                gameproc()
            else:
                input(Fore.RED + 'Ты явно что-то не так написала')


def waychoise():
    global health, inventory, meetshop1, mvtype, maptoct
    print(Fore.LIGHTWHITE_EX + 'Куда идем?')
    print('1) Ищем приключения')
    print('2) Посмотреть характеристики')
    print('3) Открыть рюкзак и полечиться')
    if meetshop1 == 1:
        print('4) К торговцу')

    if ctticket == 1 or maptoct == 1:
        print('5) В город')

    waychoiser = input()
    if waychoiser == "1":
        event()
    elif waychoiser == "2":
        showparameters()
        waychoise()
    elif waychoiser == "3":
        showinv()
        healing()
        waychoise()
    elif waychoiser == "4" and meetshop1 == 1:
        meetshop()
    elif waychoiser == "5" and ctticket == 1:
        meetcity()
    elif waychoiser == "5" and maptoct == 1 and ctticket == 0:
        meettreasure(mv15)
    elif waychoiser == "6":
        meetshop()
    else:
        input(Fore.RED + 'Выбери число из списка')
        waychoise()


def event():
    global meetshop1
    event = r.randint(1, 100)
    if meetshop1 ==1:
        if event >= 1 and event <= 5:
            meetshop()
        if event >= 6 and event <= 40:
            meetfight()
        elif event >= 41 and event <= 100:
            meettreasure(0)
    else:
        if event >= 1 and event <= 10:
            meetshop()
        elif event >= 11 and event <= 55:
            meetfight()
        elif event >= 56 and event <= 100:
            meettreasure(0)


def cls():
    print("\n" * 100)


def gameproc():

    global health
    global money
    global map
    global enemycounter
    global ctticket

    if map == 1:
        input(Fore.BLUE + 'Теперь у тебя есть карта.')
        input('На ней чётко нарисован портал в паре дней от тебя')
        input('Ты прошла эти пару дней без приключений и увидела портал на своём пути')
        input('Зайдя в него ты просунулась в своей постели')
        endgame()
    if health <= 0:
        showec()
        if input(Fore.LIGHTRED_EX + 'ну че, сначала?\n').lower() == 'да':
            cls()
            initgame()
        else:
            sys.exit()
    else:
        waychoise()


def endgame():
    while health > 0:
        input('Вау, да ты же прошла игру... просто вау!')
        if input('Ну че сначала?:) ').lower() == 'да':
            cls()
            initgame()
        else:
            sys.exit()


initgame()