# module naming_convention_prac

public_variable = 1
_private_variable = 1/2  

"""
If we do: import naming_convention_prac
We can access both variables like this:
>>> naming_convention_prac.public_variable
>>> naming_convention_prac._private_variable

If we do: from naming_convention_prac import *
We can access only the variables not starting with single undersccore:
>>> public_variable

"""