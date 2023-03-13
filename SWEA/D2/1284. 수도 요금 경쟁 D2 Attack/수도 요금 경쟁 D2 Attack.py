t=int(input())

for _ in range(1, t+1):
    n=list(map(int, input().split()))
    p, q, r, s, w = n
    res=0

    cost_a = p * w
    cost_b = q

    if w > r:
        cost_b += (w - r) * s

    if cost_a <= cost_b:
        res = cost_a
    else:
        res = cost_b

    print(f'#{_} {res}')
