a=int(input())
b=int(input())
c=list(str(b))
d=[]
e=[]

for _ in range(1, len(c)+1):
    _=-_
    i=0
    i=a*int(c[_])
    d.append(i)

for elem in range(0, len(d)):
    j=d[elem] * 10**elem
    e.append(j)


print(*d, sep='\n')
print(sum(e))