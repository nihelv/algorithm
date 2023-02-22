t=int(input())

for _ in range(1, t+1):
    n=list(input())
    n1=list(reversed(n))
    if n == n1:
        res=1
    else:
        res=0
    
    print(f'#{_} {res}')