from math import ceil

class Room:
    def __init__(self,width,lenght,height):
        self.width=width;
        self.lenght=lenght;
        self.height=height;
        self.wd=[];

    def add_wd(self,width,height):
        self.wd.append(WinDoor(width,height));

    def get_square(self):
        return 2 * self.height * (self.width+self.lenght);

    def get_work_surface(self):
        square=self.get_square();
        for i in self.wd:
            square-=i.get_square();
        return square;

    def get_number_of_rolls(self,lenght,width):
        oneRollSquare=lenght*width;
        workSquare=self.get_work_surface();
        return ceil(workSquare/oneRollSquare);s

class WinDoor:
    def __init__(self,width,height):
        self.width=width;
        self.height=height;

    def get_square(self):
        return self.width * self.height;