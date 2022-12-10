from math import floor

class Snow:
    def __init__(self,count):
        self.count=count;
    
    def makeSnow(self,countLine):
        result='';

        for i in range(1,int(self.count)):
            result+="*";
            if(i%countLine==0):
                result+="\n"

        result+="*";

        print(result);

    def __add__(self,b):
        self.count+=b;
        print("Было добавлено " + str(b) + " снежоков \n");
    def __sub__(self,b):
        self.count-=b;
        print("Было убрано " + str(b) + " снежоков \n");
    def __mul__(self,b):
        self.count*=b;
        print("Количество снежком было увеличено в " + str(b) + " раз \n")
    def __truediv__(self,b):
        self.count=floor(self.count/b);
        print("Количество снежком было уменьшено в " + str(b) + " раз \n")



snow=Snow(5);
snow+1;
snow-1;
snow*5;
snow/2;
snow.makeSnow(4);
