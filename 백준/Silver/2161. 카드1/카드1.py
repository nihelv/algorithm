num=int(input())

list_c=[i for i in range(1, num+1)]
leave_c=[]

for n in range(1, num+1):
    if len(list_c) != 1:
        leave_c.append(list_c.pop(0))
        list_c.append(list_c.pop(0))
    elif len(list_c)==2:
        leave_c.append(list_c.pop(0))
    elif len(list_c) == 1:
        break

for n2 in leave_c:
    print(n2, end=' ')

print(*list_c)