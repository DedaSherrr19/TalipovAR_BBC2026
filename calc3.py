def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calc(a,f,b):
    if f=='+':
        print(plus(a,b))
    if f=='-':
        print(minus(a,b))
    if f=='/':
        print(divide(a,b))
    if f=='*':
        print(multiply(a,b))
while True:
    a=int(input("аргумент 1: "))
    f=input("оператор: ")
    b=int(input("аргумент 2: "))

    print("результат: ")
    calc(a,f,b)
