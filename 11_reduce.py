# from functools import reduce
# def sum(a,b):
#     return a+b

# numbers=[2,2,5,8,9,8]
# #       [4,5,8,9,8]
# #       [9,8,9,8]
# #       [17,9,8]
# #       [26,8]
# #       [34]
# c=reduce(sum,numbers)
# print(c)
from functools import reduce
def substract(a,b):
    return a-b
numbers=[11,22,59,86,32,25,26,53,35,21]
'''
        [-11,59,86,32,25,26,53,35,21]
        [-70,86,32,25,26,53,35,21]
        [-159,32,25,26,53,35,21]
        [-191,25,26,53,35,21]
        [-216,26,53,35,21]
        [-242,53,35,21]
        [-295,35,21]
        [-330,21]
        [-351]
'''
c=reduce(substract,numbers)
print(c)

def multilpy(a,b):
    return a*b
numbers=[2,3,4,5,6]
'''     [6,4,5,6]
        [24,5,6]
        [120,6]
        [720]
'''
new=reduce(multilpy,numbers)
print(new)
