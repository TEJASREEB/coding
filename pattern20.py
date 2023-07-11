# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * * * *  
 
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *  
           
n = int(input())
for i in range(n):
    print((i+1) * "* ")
print(n * " ")
for j in range(n,-1,-1):
    print(j * "* ")
    