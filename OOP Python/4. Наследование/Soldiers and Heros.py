from random import choice

class Unit:
    def __init__(self,number,team):
        self.number=number
        self.team=team

class Hero(Unit):

    def levelup(self):
        if(hasattr(self,'level')):
            self.level+=1
        else:
            self.level=1

        print('Уровень героя №' + str(self.number) + ' увеличелся, текущий уровень героя ' + str(self.level))

class Soldier(Unit):
    def followToHero(self,hero):
        print('Создат следует за героем №' + str(hero.number))


RedHero=Hero(1,'red')
BlueHero=Hero(2,'blue')

units={'red':[],'blue':[]};

for i in range(3,30,+1):
    soldier=Soldier(i,choice(['red','blue']))
    units[soldier.team].append(soldier)

if len(units['red'])>len(units['blue']):
    RedHero.levelup()
    print('Уровень красного героя ' + str(RedHero.level))
else:
    BlueHero.levelup()


units['red'][0].followToHero(RedHero)