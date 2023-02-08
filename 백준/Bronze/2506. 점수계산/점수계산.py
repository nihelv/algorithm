t=int(input())
s=list(map(int, input().split()))

r=0
b=0

for _ in range(t):
    if s[_] == 1:
        r += 1
        
        if 1 <= _ and s[_-1] == 1:
            b += 1
            r += b
        else:
            b=0

print(r)