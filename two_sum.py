nums = list(map(int,input().split()))
target = int(input())
for i in range(len(nums)):
    p = target-nums[i]
    if p in nums:
        print(nums.index(p),i)
        break
else:
    print("not found")
