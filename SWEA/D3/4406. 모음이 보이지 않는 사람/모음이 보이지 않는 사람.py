t=int(input()) # t = 테스트 케이스 = input 받은 1자리 정수

a=['a', 'e', 'i', 'o', 'u']
for _ in range(1, t+1):
    w=input()
    for s in w:
        if s in a:
            w=w.replace(s, '')
    
    print(f'#{_} {w}')