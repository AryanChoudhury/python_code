dic = {"Aryan": "human", "spoon":object,}
print(dic["Aryan"])

dict = {344:"Aryan", 56:"Raju", 60:"neha"}
print(dict[56])


info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  