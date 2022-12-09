def add():#this is a defination of the function where a and b are parameters
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("sum: ",a+b)

add()#function calling.here the a,b are positional arguments whereas in starting parameters

def add(x,y):#function defination with parameters but not manadtory for the parameters and arguments to be equal
    print("sum: ",x+y)#positional arguments

a=int(input("enter the first term: "))
b=int(input('enter the second number: '))
add(a,b)
#error could be seen when there is no parameters but arguments given by the user.....

def add(x,y):
    print("sum: ",x+y)
def sub():
    b=int(input("enter the first number: "))
    a=int(input("enter the second integer: "))
    print("sub: ",b-a)
def calc():
    num1=int(input("enter the first integer: "))
    num2=int(input("enter the second integer: "))
    mul=num1*num2
    add=num1+num2
    sub=num1-num2
    return(mul,sub,add)#give a value in return to the variable as result

a,b,c= calc()
print("multiplication answer: ",a,"\n","addition: ",b,"\n","subtraction: ",c)#three value to be returned while named as a,b,c
"""we can only write retrun statement only once. the keyword def is only to be written. every function need no tot have 
return value."""
def abc():
    """function is defined to print string abc.this is a comment inside a function"""
    a=10
print(abc.__doc__)#docstring function is used to read a comment inside a function
#no expression in function it would show none
def pqr():
    """function is defined to print docstring"""
    a=10
    return

print(pqr.__doc__)
b=abc()
#argument function passsed to a function by the user
#parameter function passed by a function to a user

#LOCAL AND GLOBAL SCOPE
a=10#global
def abc():
    a=20
    #global a#local
    #global a=20 it willl show error because it is not valid syntax
    print("a= ",a)
print("value of A outside function: ",a)
abc()#it is updated to local due to it it prints local variable
print("value of A outside function: ",a)#it is because value doesn't change

"""def sayhello(s):
    greet="Hello"
l1=["ram","mohan","shyam","uma"]
for i in range(len (l1)):
    sayhello(),printl1[i])"""
def display(name,age):
    print("name is: ",name,"\n","age is : ",age)#\n to new line
display('j',25)
display(40,'s')#the first value is given to name and then the secon dto secon
display("john",223)#if there will be only john then syntax typevalue error
display(age=23,name="rahul")#keyword argument the value assign will be alloted to the same variable

#DEFAULT ARGUMENT
def display(a,b=10,c=20):#b and c default argument value and a is positional argument
    print("a=",a,"b=",b,"c=",c)

display(15,67)
#to give default value we have to start from RIGHT AND INTERPRETER READS FROM RIGHT TO LEFT
"""def display(a,b=10,c):
    print("a=",a,"b=",b,"c=",c)
display(15,67)
it will show error due to about argument"""
def display(a,b,c=10):
    print("a= ",a,"b= ",b,"c= ",c)
display(12,23)
display(12,23,24)
display(15,c=67)
