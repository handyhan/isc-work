a = set(range(5))
print a

b = set(range(2,9,2))
print b

print a|b
print a & b

band = ['mel','geri','victoria','mel','emma']

counts = {}

for member in band:
    if member not in counts:
        counts.setdefault(member,1)
    else:
        counts[member] += 1

for member in counts:
    print member,counts[member]

if {}: print 'hi'

d = {'maggie':'uk','ronnie':'usa'}
print dir(d)

print d.items() ,  d.keys() ,d.values()

d.get('helen'['germany'])
print d
