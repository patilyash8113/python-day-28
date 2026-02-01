# # def is_smaller_than_9(x):
#     # if x<9:
#     #     return True
#     # else:
#     #     return False
# a=[65,5,89,8,10,11,52,3,6,8,89,100,9]
# new = list(filter(lambda x:x<9,a))
# print(new)

def is_grater_than_10 (x):
    if x>10:
        return True
    elif x==50:
        return True or False
    else:
        return False
num=[12,10,22,33,96,86,75,45,65,451,10,11,9,8,7,50,50]
new=list(filter(is_grater_than_10,num))
print(new)
