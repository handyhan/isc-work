mylist = range(1,6)

print mylist[1]
print mylist[-2]

print mylist[:]
print mylist[1:4] 

one_to_ten = range(1,11)
print one_to_ten

one_to_ten.append(11)
print one_to_ten

one_to_ten.extend([12,13,14])
print one_to_ten

forward = []
backwards = []

values = (["a","b","c"])

for i in values:
   forward.append(i)
   backwards.insert(0,i)


print forward,backwards

backwards.reverse()

print forward,backwards

countries = ["uk","usa","uk","uae"]
print dir(countries)


print countries.count("uk")
