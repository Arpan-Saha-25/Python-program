def game():
    return 6156


score = game()

with open("E:\python_beginning\prog_of_py\highscore.txt",'r') as f:
    highscore = f.read()

if int(highscore) < score  or highscore=='':
    with open('E:\python_beginning\prog_of_py\highscore.txt','w') as f :
        f.write(str(score))

