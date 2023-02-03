n=int(input())
m=list(map(int, input().split()))

m1=sorted(m)
res=len(m1)//2

print(m1[res])