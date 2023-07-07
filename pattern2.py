# 11111
# 2222
# 333
# 44
# 5

rows = int(input())
for i in range(rows,0,-1):
    for j in range(i):
        print(rows-i+1,end="")
    print("")