num = int(input())

for i in range (1, num + 1, 1) :
    if i%10 in [3, 6, 9]:
        print("X", end=" ")
    else :
        print(i, end=" ")
