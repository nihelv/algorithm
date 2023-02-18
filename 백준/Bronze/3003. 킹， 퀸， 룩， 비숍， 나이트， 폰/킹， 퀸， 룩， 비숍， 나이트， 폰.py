n=list(map(int, input().split()))


c=[1, 1, 2, 2, 2, 8]
c1=[]
if n != c:
    for _ in range(len(n)):
        if n[_] < c[_]:
            c1.append(c[_] - n[_])
        elif n[_] > c[_]:
            c1.append(c[_] - n[_])
        else:
            c1.append(0)

print(*c1)