t=10

for _ in range(1, t+1):
    n=int(input())
    nums=list(map(int, input().split()))
    for i in range(n):
        mh=max(nums)
        nh=min(nums)
        mhi=nums.index(mh)
        nhi=nums.index(nh)
        nums[mhi] -= 1
        nums[nhi] += 1
    res=max(nums) - min(nums)
    print(f'#{_} {res}')