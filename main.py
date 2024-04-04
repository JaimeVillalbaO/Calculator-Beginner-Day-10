from acsi_day10 import logo
import os



def add (a, b):
    return a + b

def substraction (a, b):
    return a - b

def mult(a, b):
    return a * b

def div (a, b):
    return a / b


operations = {
    '+' : add ,
    '-' : substraction ,
    '*' : mult , 
    '/' : div ,
}


def calculator():
    print(logo)
    num1 = float(input('What is the first number ?: '))

    for k in operations:
        print (k)

    exit = 'yes'
    while exit == 'yes':

        operator = input('Pick an operaton: ')
        num2 = float(input('What is the next number ?: '))
        result = operations[operator](num1 , num2)
        print(f'Operation: {num1} {operator} {num2} = {result}')
        
        
        exit = input(f'type "yes" to continue calculating with {result}, or type "no" to exit, or type "new" to star again: ')   
        
        if exit == 'no':
            continue
        elif exit == 'yes':
            num1 = result
        elif exit == 'new':
            os.system('cls') 
            calculator()

calculator()
 