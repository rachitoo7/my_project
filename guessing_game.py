import math
import random
# import libraries
# store lower and upper limit in bariable
lower = int(input('lower bound '))
upper = int(input('upper bound '))

# store random number in x
x = random.randint(lower,upper)

# limit the chance to guess
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

# if max chance gate over 
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")           
    



