from random import randint

l = []

def random_average(n):
    for i in range(n):
        rnd = randint(1, 100)
        l.append(rnd)
    print(l)
random_average(11)
suma = sum(l)
quantity = len(l)
avg = suma / quantity
print(f"średnia wynosi {avg} ilosc = {quantity}")