with open("E:\python_beginning\prog_of_py\sample1.txt","r") as f:
    content = f.read()

content=content.replace("hell","%*^%&*@")

with open("E:\python_beginning\prog_of_py\sample1.txt","w") as f:
    f.write(content)

