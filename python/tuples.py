t = (1,)
print t[-1]

nums=tuple(range(100,201))

print nums[0],nums[-1]

mylist=[23,"hi",2.4e-10]

for (count,item) in enumerate(mylist):
   print count,item


first, middle, last = mylist  # tuple on RHS only exists as tuple on this like! is a smart way to unpack sing a,b,c is interprated as a tuple, once line is left items of the tuple are variables of type they have been assigned from the list

print first,middle,last

first,middle,last=middle,last,first
