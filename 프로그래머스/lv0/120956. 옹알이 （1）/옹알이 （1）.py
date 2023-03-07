def solution(babbling):
    answer = 0
    bb =['aya','ye','woo','ma']
    rep=[]
    for i in babbling:
        for j in bb:
            i=i.replace(j,'*')
        rep.append(i)

    cnt=0
    for i in rep:
        i=set(i)
        if len(i)==1 and '*' in i:
            cnt+=1

    answer=cnt
    return answer