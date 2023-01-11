h=input()
# 헤드라인 문자열 입력
# 공백은 무조건 언더스코어로 입력하는 규칙인가?
u=[]
result=""
 

for i in h:
    if (1 <= len(h)) * (len(h) <= 80):
        if i.islower() == True :
            w=i.upper()
            u.append(w)
        else:
            w=i
            u.append(w)
    result += w


print(result)