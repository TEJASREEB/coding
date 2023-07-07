# 54321
# 4321
# 321
# 21
# 1

n = int(input())
for i in range(n):
    for j in range(n,i,-1):
        print(j-i,end="")
    print()