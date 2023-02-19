t = int(input())
for _ in range(1, t+1):
    n = list(map(int, input().split()))
    max_num = n[0]
    min_num = n[0]
    nmax=max(n)
    nmin=min(n)
    n.remove(nmax)
    n.remove(nmin)
    
    print(f'#{_}', round(sum(n)/len(n)))