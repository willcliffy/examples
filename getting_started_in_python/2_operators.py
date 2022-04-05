### 3. OPERATORS

# There are many operations that can be performed on variables.

# The operations that can be performed on a variable DEPENDS ON THAT VARIABLE'S TYPE

# booleans have a whole system of algebra, but we'll focus on the basic operators:

var_true  = True and True
var_false = True and False
var_false = False and False

var_true  = True or True
var_true  = True or False
var_false = False or False

# "numeric" types (integers and floats) have common arithmetic operations:
# addition, subtraction, multiplication, division, and modulo
add = 1 + 2 # 3, type integer
sub = 1 - 2 # -1, type integer
mul = 1 * 2 # 2, type integer
div = 1 / 2 # 0.5, type float
mod = 1 % 2 # 1, type integer

# strings have several operators, including concatenation, repetition, and slicing

# concatenation is the process of joining two strings together
concat = "hello" + " " + "world" # "hello world"

# repitition is the process of repeating a string or a character a certain number of times
repeat = "hello" * 3 # "hellohellohello"

# slicing is the process of taking a string and returning a substring
substring = "hello, world"[0:5] # "hello"
