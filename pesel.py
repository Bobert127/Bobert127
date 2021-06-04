def validate_pesel(p):
    s = str(p)
    sm = map(int, s)
    dl = list(sm)
    waga = int(dl[0]) * 1 + int(dl[1]) * 3 + int(dl[2]) * 7 + int(dl[3]) * 9 + int(dl[4]) * 1 + int(dl[5]) * 3 + int(
        dl[6]) * 7 + int(dl[7]) * 9 + int(dl[8]) * 1 + int(dl[9]) * 3
    modulo = waga % 10
    roznica = 10 - modulo
    if int(dl[10]) == roznica:
        print("true")
    else:
        print("fales")


validate_pesel(73042908779)