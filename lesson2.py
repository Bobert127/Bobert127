from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Podaj liczbę:")
    num = int(str_num)
    if num == rnd:
        print("Brawo!")
        guessed = True
    elif num > 11:
        print("liczba poza zakresem")
    else:
        print("Pudło!")
