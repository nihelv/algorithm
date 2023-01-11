h=input()
result=""

for i in h:
    if (1 <= len(h)) * (len(h) <= 80):
        if i.islower() == True :
            w=i.upper()
        else:
            w=i
    result += w

print(result)