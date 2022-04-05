"""
TODO - explanations of control flow are pretty weak here by comparison to the other files here

I think this is a good time to supliment with exercises.
Much easier to get used to control flow by playing with it than it is by reading about it.
"""


### 4. CONTROL FLOW

# I. The `if` statement

# there are several ways to control the flow of a program.
# the most common is the `if` statement
condition = True

if True:
    print("condition is True")

if False:
    print("this will never run")


# elif is an `else if` statement. It is used to add additional conditions to
# the `if` statement.
var_number = 3

if var_number == 1:
    print("var_number is 1")
elif condition:
    print("var_number is not 1, and var_condition is true")

# else is an `else` statement. It is used to add an additional condition to the
# `if` statement.

# TODO - This is a bad explanation of elif and else statements
if var_number == 1:
    print("var_number is 1")
else:
    print("var_number is not 1")

# note that you can chain together many elif statements and put an else at the end.
# this is useful for more complex control flow.
if var_number == 1:
    print("var_number is 1")
elif var_number == 2:
    print("var_number is 2")
elif var_number == 3:
    print("var_number is 3")
else:
    print("var_number is not 1, 2, or 3")


# II. Loops

# Loops are used to repeat an action. There are 2 different kinds of loops.


# IIa. The `for` loop

for i in range(0, 10):
    print(i) # prints 0 through 9

# the default `step` value is 1, but you can change it to any number
for i in range(0, 10, 2):
    print(i) # prints 0, 2, 4, 6, 8

# ... including floats
for i in range(0, 10, 2.5):
    print(i) # prints 0, 2.5, 5, 7.5

# note that range(x, y) is a `function` that returns a `list`. More on
# functions later, but this means that you can `iterate` over any list:
for i in [1, 5, 100]:
    print(i) # prints 1, 5, 100

var_list = [1, 2, 3]
for i in var_list:
    print(i) # prints 1, 2, 3


# IIIb. The `while` loop

# the other kind of loop is the `while` loop
# this loop will execute as long as the condition is true
var_number = 0

while var_number < 10:
    print(var_number)
    var_number += 1
# will print 0 through 9

print(var_number) # prints 10
