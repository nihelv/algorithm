a = int(input())
b = int(input())
d = [a * int(i) for i in reversed(str(b))]
result = sum(d[i] * 10**i for i in range(len(d)))
print(*d, sep='\n')
print(result)
