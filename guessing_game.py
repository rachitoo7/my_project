import math
import random
lower = int(input('lower bound '))
upper = int(input('upper bound '))
x = random.randint(lower,upper)
print('\n\tyou have',math.log(upper-lower + 1,2),'chance to guess the number\n')
count = 0
while count < math.log(upper-lower + 1,2) :
    b = int(input('guess the nomber: '))
    if b  == x :
        print('you won')
        break
    elif b > x :
        print('your no. is too big')
    elif b < x :
        print('your no. is too small')
    count += 1

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")           
    



