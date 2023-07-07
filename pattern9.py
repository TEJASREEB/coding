# 1 
# 3 2 
# 6 5 4 
# 10 9 8 7 

n = 10
num = 0
for i in range(n//2):
    k = num+i
    for j in range(i):
        print(k,end=" ")
        k=k-1
        num=num+1
    print()