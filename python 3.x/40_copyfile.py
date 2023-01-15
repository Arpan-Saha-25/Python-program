with open("E:\python_beginning\prog_of_py//this.txt","r") as f:
    content = f.read()

with open("copy.txt","w") as f:
    f.write(content)

