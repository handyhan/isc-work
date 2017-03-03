def double_it(number):
   return 2 * number

print double_it(2),double_it(1.5),double_it('bob')

def calc_hypo(a,b):
    print type(a),type(b)
    if (type(a) or  type(b)) not in (float,int):
        print "I'm not a number"
    elif a or b < 0:
        print "I'm a negative number"
    else:
        hypo = (a**2 + b**2)**(0.5)
        return hypo

print calc_hypo(-3,4)


