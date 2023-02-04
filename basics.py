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


a='hello in single quotes'
print(a)
b="hello in double quotes"
print(b)
c="""Hi.
This is a multiline string,
that is written in many lines."""
print(c)

"""
strings (str) in python is surrounded by either single quotes or double quotes.
Encase multi-line str variables in triple quotes.
Python does not have a character data  type, it is a string with a length of 1.
len() function => gives length of a string or list
"""

a="ABCDEF"
print(a[1])
print(len(a))

c=[1, 2, 3, 4]
print(type(c)) #<class 'list'>
print(len(c))
print(c[0])

a=9
b=10
print(a<b)
print(a==b)
print(a>b)

"""
Spaces are the preferred indentation method. Tabs should be used solely to 
remain consistent with code that is already indented with tabs. 
Python disallows mixing tabs and spaces for indentation.
"""

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

"""
The bool() function allows you to evaluate any value. It also gives True or False in return
Almost all values are true:
(1) str => any string is true except for empty strings
(2) int, float => any number is true except for 0
(3) list, tuples, set => any list tuple or set is true, except for the ones that have nothing in them 
"""
print(bool("Hello"))
print(bool(""))   # False
print(bool(2))
print(bool(0))    # False
print(bool(3.4))
print(bool(0.0))  # False
print(bool([1, 2, 3]))
print(bool([0]))
print(bool([]))   # False
print(bool({}))   # False
print(bool(()))   # False
print(bool(None)) # False

"""
Set is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
"""

print(type({}))  #<class 'dict'>
print(type({1})) #<class 'set'>
print(type(()))  #<class 'tuple'>
print(type([]))  #<class 'list'>


"""
Lists are ordered, their values can be changed and can also contain duplicate values
The elements in the list can be of any data type. Also we can have multiple data types in the same list

Tuples are same as list, but they cannot be changed.
We can create a tuple with a a single element by giving a comma at the end, otherwise python won't recognise it as a typle

Sets are unordered, unindexed, and do not store duplicate values

Dictionaries store key-value pairs.
Dictionaries are ordered from python3.7, earlier it was unordered.
Dictionaries don't allow duplicate keys
"""

a=[1,2,3] #list
print(a)
print(len(a))
print(a[1])

b=(1,)  #tuple with a single element
print(b)
print(type(b))
c=(1)
print(c)
print(type(c))

d={2,1,3,1}  #set
print(d)  # {1, 2, 3} : sets are unordered and unindexed
print(type(d))
print(len(d))  # 3: sets do not store duplicates

e={"apple":1, "banana":3, "mango":4, "mango":5}
print(e)
print(len(e))  # dosen't store duplicates
# print(e[1]) # key not present then error
print(e["mango"])  # the last value for the same key is stored
