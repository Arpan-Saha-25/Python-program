f = None 
for i in range(5):
    with open('E:\\python_beginning\\prog_of_py\\55_exmtrials.py','r') as f:
        if i > 2: break 

print(f.closed)