def safe_get(l, i):
    try:
        i =  3
        i = i - 1
        l = [7,2,8,2,11, 19, 87, 15, 3]
        print(l[i])
    except:
        print("None")
safe_get([1,2,3],1)