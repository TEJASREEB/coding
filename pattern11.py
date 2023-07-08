# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1 

n = int(input())
a = [[0 for x in range(n)]
        for y in range(n)]
 
for i in range(0,n):
    for j in range(0,i+1):
        if j==0 or j==i:
            a[i][j]=1
            print(a[i][j],end=" ")
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]
            print(a[i][j],end=" ")
    print()