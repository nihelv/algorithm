t=int(input())


for _ in range(1, t+1):
    n=int(input())
    a=list(map(int, input().split()))
    
    res=0
    m=a[-1]
    
    for i in range(n-2, -1, -1):
        if a[i] > m:
            m=a[i]

        else:           
            res += m-a[i]

    print(f'#{_} {res}')