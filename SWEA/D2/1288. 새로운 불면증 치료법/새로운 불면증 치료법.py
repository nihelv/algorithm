t=int(input())

for _ in range(1, t+1):
    n=int(input())
    x=0
    ml=[]
    check_list=list(range(10))
    while True:
        
        if ml == check_list:
            print(f'#{_} {x*n}')
            break

        else:
            x+=1
            managed_list=list(map(int, sorted(set(str(x*n)))))
            ml+=managed_list
            ml=sorted(set(ml))
            continue