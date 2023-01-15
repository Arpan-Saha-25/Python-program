'''Password generator in PYTHON '''

import random
def pswd():

    print("A good password for you is : " ,end='')
    for i in range(8):
        a = random.choice('abcdef123045ghijkl87mnopqrstuvwxyz69')
        y = random.choice("!@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print(a+y,end='')
    return ''

#calling our function 
pswd()