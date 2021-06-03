def divide(a, b):
    try:
        if a or b == int:
            return a / b

    except:  # niewłaściwy typ

        print(f"liczba {a} or {b} nie jest naturlana")


dane = divide(3, 5)

print(dane)
