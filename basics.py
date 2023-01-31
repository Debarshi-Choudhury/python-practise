"""
Python is both a strongly typed and a dynamically typed language. 
Strong typing means that variables do have a type 
and that the type matters when performing operations on a variable. 
Dynamic typing means that the type of the variable is determined only during runtime.
"""

a=31  #the variable is created when you first assign a value to it
print(a)
print(type(a))

"""
Built-in Data types in Python:
Text: str
Numeric: int, float
Sequence: list, tuple, range
Boolean types: bool
"""

b=str(a) #typecasting an int to str
print(b)
print(type(b))

c=float(a)
print(c)
print(type(c))

d="45"
e=int(d)
print(e)
print(type(e))

a=str(a) #the type of a variable can change later on during execution
print(type(a)) 

"""
One of the key features of Python is that everything is an object, and the type is just one attribute of an object.
Use dir() built-in function to see all attributes of the object
"""

a=1
print(dir(a))

"""
The fact that everything is an object means that there is a lot of “unboxing”
and “boxing” involved when Python performs operations with variables. Forexample, when just adding two integers

a = 7
b = 6
c = a + b
there are several steps Python needs to do:

Check the types of both operands
Check whether they both support the + operation
Extract the function that performs the + operation (due to operatoroverloading objects can have a custom definition for addition)
Extract the actual values of the objects
Perform the + operation
Construct a new integer object for the result
"""

