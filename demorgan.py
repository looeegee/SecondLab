#p = set([True, True, False, False])
#q = set([True, False, True, False])

#x = not(p&q)==(not p) | (not q)
#y = not(p | q)==(not p) & (not q)
#print('x is :', x, '\ny is :' ,y)

p = True
q = True
print(not(p or q) == ((not p) and (not q)))

p = True
q = False
print(not(p or q) == ((not p) and (not q)))

p = False
q = True
print(not(p or q) == ((not p) and (not q)))

p = False
q = False
print(not(p or q) == ((not p) and (not q)))