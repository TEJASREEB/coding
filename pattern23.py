# ****************
# *******__*******
# ******____******
# *****______*****
# ****________****
# ***__________***
# **____________**
# *______________*

n = int(input())
for i in range(n):
    if i == 0:
        print((2*n) * "*")
    else:
        print((n-i) * "*" + 2 * i * "_" + (n-i) * "*") 
