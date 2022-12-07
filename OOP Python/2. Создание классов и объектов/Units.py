import random;

class Unit:
    def __init__(self,name):
        self.health=100;
        self.name=name;

    def damage(self,enemyName):
        print(self.name + ' был атакован ' + enemyName)
        self.health-=20;

        if(self.health<=0):
            print(self.name + ' погиб, ' + enemyName + ' победил!');

firstUnit=Unit('Первый юнит');
secontUnit=Unit('Второй юнит');

while firstUnit.health>0 and secontUnit.health>0:
    whoHit=random.randrange(0,2);
    if (whoHit==1):
        firstUnit.damage(secontUnit.name);
    else:
        secontUnit.damage(firstUnit.name);
    print('-----------------------')