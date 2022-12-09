class Math:
    def __init__(self,a):
        self.a=a;

    def __add__(self, b):
        res = self.a+b;
        print( str(self.a) + '+' + str(b) + '=' +  str(res));

a=Math(5);

a+4;