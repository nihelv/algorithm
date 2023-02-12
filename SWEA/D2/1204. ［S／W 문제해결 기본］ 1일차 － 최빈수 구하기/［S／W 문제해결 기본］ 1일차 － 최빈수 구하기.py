T = int(input())
# T=1

for test_case in range(1, T + 1):
    tem={}
    test_num=int(input())
    # test_num=1
    input_v=list(map(int, input().split()))
    for num in input_v:
        o=input_v.count(num)
        tem[o]=num

    print(f'#{test_num} {tem.get(max(tem))}')