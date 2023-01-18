t=int(input())

for i in range(1, t+1):
    r, s=input().split()
    p=[]
    for elem in s:        
        result=elem*int(r)
        p.append(result)
        P=''.join(p)
    print(P)