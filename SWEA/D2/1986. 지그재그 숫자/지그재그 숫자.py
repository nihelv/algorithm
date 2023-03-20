T=int(input())

for _ in range(1, T+1):
    N=int(input())
    numlist=[]
    for i in range(1, N+1):
        if i % 2 == 1:
            numlist.append(i)
        else:
            numlist.append(-i)
        
    print(f'#{_} {sum(numlist)}')