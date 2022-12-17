from random import randrange

def Random(count,dia):
    for i in range(count):
        yield randrange(dia)

d = Random(5,10)

print(next(d))
print(next(d))
