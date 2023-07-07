# 012345
# 01234
# 0123
# 012
# 01

rows = int(input())
for i in range(rows+1,1,-1):
    for j in range(i):
        print(j,end="")
    print("")