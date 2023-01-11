p1, p2 = list(map(int,input().split()))
l1=[p1, p2]

for g in l1:
    if (p1 != (p2+1)%3) :
        print("A")
    elif (p1 == (p2+1)%3) :
        print("B")
    else:
        print('error')