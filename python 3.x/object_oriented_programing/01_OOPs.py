#a = 12
#b = 34

#print("The sum of a and b is ",a+b)

class number:
    def sum(self):
        return self.a + self.b
num = number()
num.a = 12
num.b = 34
s = num.sum()

print(s)