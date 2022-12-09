class PrivateData:
    def __init__(self,name):
        PrivateData.__name=name;

    def setName(self,name):
        PrivateData.__name=name;

    def getName(self):
        return PrivateData.__name;

name=PrivateData('Alex');
print(name.getName());
name.setName('Mike');
print(name.getName());