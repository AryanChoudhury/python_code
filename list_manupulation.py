l = [2,5,4,8,8]
print(l)
l.append(1)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l.index(4))
print(l.count(4))
l.insert(1,899)
print(l)

m = [100,200,300,500,10000]
l.extend(m)
print(l)