#55555
# 4444
# 333
# 22
# 1

n = int(input())
for i in range(n):
    for j in range(n,i,-1):
        print(n-i,end="")
    print()