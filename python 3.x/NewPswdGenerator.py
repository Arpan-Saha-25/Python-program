'''Password generator in PYTHON '''

import random
def pswd():
    print("A good password for you is :" ,end=' ')
    for i in range(8):
        a = random.choice('abcdefghijklmnopqrstuvwxyz1230456987')
        y = random.choice("!@#$%&")
        print(a+y,end='')
