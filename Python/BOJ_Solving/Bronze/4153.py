while True :
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0 and b == 0 and c == 0 :
        break
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        print("right")
    else : print("wrong")
