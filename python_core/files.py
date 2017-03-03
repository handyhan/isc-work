
with open("weather.csv",'r') as reader:
    line = reader.readline()
    print line
    while line:    	#as line as line has something in it this is True
        line = reader.readline()
        print line

    print "It's over"


with open("weather.csv","r") as reader:
    header = reader.readline() # these are just words giving the column titles so we want to ignor this
    rain=[]
    for line in reader.readlines():    
         r = line.strip("\n").split(",")[-1]
         rain.append(float(r))

print rain

with open("myrain.txt","w") as writer:
   writer.write(str(rain))



import struct

bin_data = struct.pack("bbbb",123,12,45,34) #convert simple data into binary form


with open("mybinary.dat","wb") as writer:
    writer.write(bin_data)


with open("mybinary.dat","r") as reader:
    bin_data2 = reader.read()
    data = struct.unpack("bbbb",bin_data2)

print data
