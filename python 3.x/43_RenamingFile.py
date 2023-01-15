import os

oldname = "E:\python_beginning\prog_of_py\copy2.txt"
newname= "Renamed_Copied.txt"
with open(oldname)as f :
    content = f.read()
with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)
