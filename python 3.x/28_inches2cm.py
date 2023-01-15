choose = int(input("Enter \n 1 for cm to inches \n 2 for inches to cm \t"))
if choose==1 :
    def convertor(cm):
        return cm/2.54

    a = int(input("Enter the value of cm = "))
    print(convertor(a))

else:
    def convert(inches):
        return inches*2.54

    a = int(input("Enter the value of inches = "))
    print(convert(a))
