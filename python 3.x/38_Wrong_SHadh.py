words = ["kaddu","mota","noob","taklu","goooo"]

with open("E://python_beginning//prog_of_py//sample1.txt","r") as f:
    content = f.read()

for i in words:
    content=content.replace(i,"#**#**#")

    with open("E://python_beginning//prog_of_py//sample1.txt","w") as f:
        f.write(content)

