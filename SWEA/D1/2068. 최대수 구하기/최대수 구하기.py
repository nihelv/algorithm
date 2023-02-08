t=int(input())

for _ in range(1, t+1):
    l=list(map(int, input().split()))
    print(f'#{_} {max(l)}')