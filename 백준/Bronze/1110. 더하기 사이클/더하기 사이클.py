n=int(input())

if n < 10:
    n=int('0'+str(n))

a = n // 10
b = n % 10
c = a + b
d = c % 10

r=1
m=int(str(b)+str(d))

while True:
    if n != m:
        x = int(str(m // 10)+str(m % 10))
        z = m // 10 + m % 10
        m = int(str(x % 10) + str(z % 10))
        r += 1
    else:
        print(r)
        break