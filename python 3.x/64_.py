try :
    
    x,y =raw_input().split()

    x = int(x)
    y = float(y)
    if x>0 and x<=2000:
        if x%5==0:
            if y>=0 and y<=2000:
                if x>y or x==y :
                    print("%.2f" % y)
                if y>x:
                    y = (y-x) 
                    if y<=0: 
                        print("%.2f" % y)
                    else:
                        y = y-0.50
                        print("%.2f" % y)
            else:print("%.2f" % y)   
        else:print("%.2f" % y) 
        
    else:print("%.2f" % y)
except :
    pass