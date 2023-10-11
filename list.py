l=[3,5,6, "Aryan", True]
print(l)
print(type(l))
print(l[1])
print(l[0])
print(l[2])
print(l[-3]) #Note: this is negetive indexing
print(l[len(l)-3]) #Note: this is positive indexing
if "Aryan" in l:
    print("yes")
else: 
    print("no")
