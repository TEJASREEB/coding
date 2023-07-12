#         * 
#        * * 
#       * * * 
#      * * * * 
#     * * * * * 
#    * * * * * * 
#     * * * * * 
#      * * * * 
#       * * * 
#        * * 
#         * 

n = int(input())
for i in range(n):
    print((2*n-i-1) * " " + (i+1) * "* ")
for j in range(n,-1,-1):
    print((2*n-j-1) * " " + (j+1) * "* ")