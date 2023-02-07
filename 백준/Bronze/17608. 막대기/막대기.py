import sys

n=int(sys.stdin.readline())

nums=[]
result=1

for _ in range(n):
    a=int(sys.stdin.readline())
    nums.append(a)


m=nums[-1]

for i in reversed(nums):
    if i > m:
        result += 1
        m=i

print(result)