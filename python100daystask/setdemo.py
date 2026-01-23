val =set()
print(type(val))
# set is nt ordered.

s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
print(s1.intersection(s2))