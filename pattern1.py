# 1 
# 12 
# 123 
# 1234 
# 12345 


rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print(j+1,end="")
    print(" ")
