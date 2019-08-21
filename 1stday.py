a = 5
b = 5
no = 12 
def sub(a , b):
    return a - b 
def add(a , b):
    return a+b
def mul(a , b ):
    return a*b
def div(a , b):
    return a/b 

def main():
    global a , b  , no
    a = input("enter a ")
    b = input("entrt b ")
    no = input("entrt no ")
    a = (float(a))
    b = float(b)
    print('Top down approach with procedure oriented code : \n ')  
    print("Addition: \n")
    print(add(a,b))
    print("Subtraction: \n")
    print(sub(a,b))
    print("Multiplication: \n")
    print(mul(a,b))
    print("Division: \n")
    print(div(a,b))
    
if __name__  == "__main__":
    main()


class Calculator :
    def __init__(self , a, b , no):
        self.a = float(a)
        self.b = float(b)
        self.no = float(no)
        
    def add(self):
        return self.a+self.b
    def sub(self ):
        return self.a-self.b
    def mul(self ):
        return self.a*self.b
    def div(self ):
        return self.a/self.b
    
    def tabels(self):
        no = self.no
        count = 0;
        tab = []
        tab2 = []
        while (count != 10):
            count = 1+count
            tab.append (count * no)
        for i in range(1, 11):
            tab2.append (i*no)
        return tab , tab2
        
    
            
    def action(self , action):
        switch  = {
            'tab'   : self.tabels(),
            'add'   : self.add(),
            'sub'   : self.sub(),
            'mul'   : self.mul(),
            'div'   : self.div(),
            'invalid' :'invalid'
            
        }
        return switch.get(action , "invalid")

print('\nObject oriented code : \n ')
cal =  Calculator(a, b , no)
print("Addition: \n")
print(cal.action('add'))
print("Subtraction: \n")
print(cal.action('sub'))
print("Multiplication: \n")
print(cal.action('mul'))
print("Division: \n")
print(cal.action('div'))
print("Table: \n")
print(cal.tabels())


def revers_str(str):
    str1 = []
    lenght = len(str)
    for i in range(lenght):
        index = lenght - i
        str1.append(str[index-1])
    s = ''
    return s.join(str1)


str = "hello word"
 
print(revers_str(str))


def larg_number(list):
    max = 0
    for i in list:
        if i > max :
            max = i 
    return max
list = [1,3 ,5 , 4, 5]
print(larg_number(list))
    
    
