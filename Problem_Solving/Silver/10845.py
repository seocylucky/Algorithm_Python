import sys

n = int(sys.stdin.readline())
d = []

for i in range(n) :
    a = sys.stdin.readline().split()

    if a[0] == "push" :
        d.append(a[1])
    elif a[0] == "pop" :
        if len(d) == 0 :
            print(-1)
        else :
            print(d.pop(0))
    elif a[0] == "front" :
        if len(d) == 0 :
            print(-1)
        else :
            print(d[0])
    elif a[0] == "back" :
        if len(d) == 0 :
            print(-1)
        else :
            print(d[len(d)-1])
    elif a[0] == "size" :
        print(len(d))
    elif a[0] == "empty" :
        if len(d) == 0 :
            print(1)
        elif len(d) != 0 :
            print(0)
