
class Person:
    def __init__(self,name,secondName,speciality=1):
        self.name = name;
        self.secondName = secondName;
        self.speciality = str(speciality);

    def __del__(self):
        print('До свидания, мистер ' + self.name + ' ' + self.secondName);

    def printPersonInfo(self):
        print(self.name + ' ' + self.secondName + ' Навык: ' + self.speciality);

person1=Person('Алекс','Фирст',3);
person2=Person('Максим','Двойка',2);
person3=Person('Андрей','Тройка',5);

person1.printPersonInfo();
person2.printPersonInfo();
person3.printPersonInfo();

del person2;

input();