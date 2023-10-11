# tup = (1,2,3,4,5,6,7,8,9,10,11)
# print (type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])

c = ("Spain", "France", "Germany", "India")
temp = list(c)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
c = tuple(temp)
print(c)
