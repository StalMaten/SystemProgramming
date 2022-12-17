from random import randrange

class Random:
    def __init__(self,count,diap):
        self.random=[]
        for i in range(count):
            self.random.append(randrange(int(diap)))

    def __iter__(self):
        return RandomIterator(self.random[:])

class RandomIterator:
    def __init__(self,numbers):
        self.numbers=numbers

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers == []:
            raise StopIteration
        item = self.numbers[0]
        del self.numbers[0]
        return item

a=Random(5,10);
print(a.random)

for i in a:
    print(i)
