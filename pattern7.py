# 1
# 21
# 321
# 4321
# 54321


n = int(input())
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()