t=int(input())

for _ in range(1, t+1):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{_}', '>')
    elif a < b:
        print(f'#{_}', '<')
    else:
        print(f'#{_}', '=')