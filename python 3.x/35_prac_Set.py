f = open('E:\python_beginning\prog_of_py\poems.txt')
t= f.read()

if 'twinkle' in t :
    print("Twinkle is present.")
else: 
    print("Twinkle is not present.")

f.close()


