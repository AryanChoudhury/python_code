# s = {2,4,5,6}
# print (s)


# info = {"carla",19, False,5.9, 19}
# print (info)

# Aryan = set()
# print(type(Aryan))

# for i in info:
#     print(i)

# s1 = {1,2,3,4}
# s2 = {3,6,7}
# print(s1.union(s2))
# s1.update(s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
print(cities.intersection(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))