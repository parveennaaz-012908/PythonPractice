lst = [1,2,4,8, 6,8,9]
#jump index
print(lst[1:9:3])
#list comprehesion
lst2=[i for i in range(4)]
print(lst2)
lst3 = [i*i for i in range(10)]
lst4 = [i*i for i in range(10)if i%2==0]
print(lst3)
print(lst4)
#list methods:
l=[23,1,4]
l.append(8)
l.sort()
l.sort(reverse=True)
l.reverse()
l.index(1)
l.count(1)
m=l
m[0]=100
print(l)
print(m)
l.insert(2,190)
print(l)