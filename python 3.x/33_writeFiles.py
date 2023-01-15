f = open('another.txt','w')
f.write("Please write this to the file")
f.close()

f=open('another.txt','a')
f.write(" \n and also appending.")
f.close()


