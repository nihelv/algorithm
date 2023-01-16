s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())                  #다섯줄 인풋
s5=int(input())

s_l1=[s1, s2, s3, s4, s5]        #for 문 돌리기 위해서 리스트
# s_l1=[10, 65, 100, 30, 95]
s_l2=[]                          #보강 듣는 조건으로 40점 처리한 리스트

for s in s_l1:
    if s <= 40:                  #40 미만이면 40점 취급, 40점도 그냥 40점
        s_l2.append(40)
    else:
        s_l2.append(s)           #40 초과면 점수 그대로

A=sum(s_l2)/5                    #s_l2를 학생 수 대로 나눈다(다섯명 제시)
print(int(A))