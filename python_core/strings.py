s = 'I love to write python'

for i in s:
    print i

print s[4]
print s[-1], len(s)

print s[0],s[0][0],s[0][0][0]


split_s = s.split(" ")
print split_s

for i in split_s:
    if "i" in i:
        print "I found 'i' in {0}".format(i)
        print i.find("i")
        print i.find("i") > -1


something = " Completely Different"
print dir(something)
print something.count("t")
print something.find("plete")

split_some = something.split("e")
thing2 = something.replace("Different","Silly")

print split_some, thing2
