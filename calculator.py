#Simple calculator

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    '+':add,
    '-':sub,
    '/':div,
    '*':mul
}

n1=int(input("Enter the first number  "))
result=n1

while(1):
    for i in operations:
        print(i)
    operator=input("Enter the operator  ")
    n2=int(input("Enter the next number  "))
    n1=result

    func=operations[operator]
    result=func(n1,n2)

    print(f"{n1} {operator} {n2} = {result}")

    ch=input("Do you want to continue with previous result? [Y/N] : ")
    if(ch=='n' or ch=='N'):
        exit()

