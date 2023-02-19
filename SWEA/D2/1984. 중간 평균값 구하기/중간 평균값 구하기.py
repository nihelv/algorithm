t=int(input())

for _ in range(1, t+1):
    n=list(map(int, input().split()))
   
    nmax=max(n)
    nmin=min(n)
    n.pop(n.index(nmax))
    n.pop(n.index(nmin))
   
    res=round(sum(n)/len(n))
    print(f'#{_} {res}')