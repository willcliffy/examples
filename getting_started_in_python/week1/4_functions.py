### 4. FUNCTIONS


# I. DEFINING AND CALLING FUNCTIONS

# A function is defined with the `def` keyword:
def function_example():
    print("hello from function")

# Functions can be "called" to execute the code inside:
function_example()
# > hello from function


# II. RETURN VALUES

# A core feature of functions is their ability to return values.
def function_with_return():
    return "hello from function_with_return"

# you can assign the return value to a variable:
return_value = function_with_return()
print(return_value)
# > hello from function_with_return

# A function can return multiple values in the form of a `tuple`
def function_with_multiple_returns():
    return "hello from", "function_with_multiple_returns"

# you can assign the return value of this function in two ways:

# - as a tuple
return_tuple = function_with_multiple_returns()
print(return_tuple)
# > ('hello from', 'function_with_multiple_returns')
print(return_tuple[0], return_tuple[1])
# > hello from function_with_multiple_returns

# - or "unpacked"
return_1, return_2 = function_with_multiple_returns()
print(return_1, return_2)
# > hello from function_with_multiple_returns


# III. PARAMETERS

# functions take values in as "parameters". Parameters are also sometimes called "arguments".
# In Python, variables can be any type. This is because Python is a "dynamically-typed" language.
def function_with_paramters(parameter1, parameter2):
    print(parameter1 + parameter2)

# When you call a function with params, you must supply the values of the parameters at the time that the function is called.
function_with_paramters(1, 2)
# > 3

# Note that you can pass different types of args into functions
function_with_paramters("hello", "string")
# > hellostring

# ... but this also means you have to be careful about what args you use when calling functions
# Try uncommenting the next line to see a potential error.
# function_with_paramters("hello", 1)
# > TypeError: can only concatenate str (not "int") to str


# IIIa. Optional Parameters

# You can provide a default value for a parameter, making it optional.

def function_with_optional_param(x = "hello from function with optional param, default"):
    print(x)

function_with_optional_param()
# > hello from function with optional param, default

function_with_optional_param("howdy bitch")
# > howdy bitch


# Z. ADVANCED NOTE: FUNCTIONS AS VALUES

# Functions are values and can be stored in variables...
x = function_example

# ... to be called later.
x()
# > hello from function

# Functions can even be passed as parameters to other functions
def call_other_function(other_function):
    other_function()

call_other_function(function_example)
# > hello from function
