### 1. VARIABLES AND TYPES

# Variables, in their simplest definition, are `symbols` that can hold `values`
# Variables in Python can hold many different `types` of `values`.


# I. Basic Types

# - There is a special `NoneType` that has exactly one value - `None`.
var_none = None

# - boolean values can be either `True` or `False`
var_true = True
var_false = False

# - integers are whole numbers (positive and negative)
var_int = 1

# - floats are numbers with a decimal point (positive and negative)
var_float = 1.0

# - strings are sequences of characters. They are usually denoted with double quotes.
var_string = "hello, world"


# II. Compound Types

# There are also more complex types of variables, such as tuples, lists, and dictionaries


# IIa. LISTS are sequences of values, and are denoted with square brackets

var_empty_list_1 = []
var_empty_list_2 = list()

var_list = [2, None, "s"]

# lists have variable length, meaning you can add to them after they are defined.
var_list.append(7.0)

# lists can also be "concatenated", or joined together:
var_concat_list = ["hello", "from", "list 1"] + ["and", "list 2"]

# Think about what this print statement will output before uncommenting it and running it
# print(var_concat_list)

# You can access particular elements in lists by `index`. Note that array indices start at 0, not 1.
print(var_list[0])
# > 2

# You can check if a particular value is in a list with the `in` keyword:
print(2 in [1, 2, 3])
# > True


# IIb. TUPLES are fixed-length (meaning once defined, their size cannot change) sequences of values

var_empty_tuple_1 = ()
var_empty_tuple_2 = tuple()

var_tuple = (1, "a", None)

# you can't append to a tuple...
# ("NO").append("AAAHHHH")
# ... but you can concatenate tuples together to get a new tuple:
var_concat_tuple = ("hello") + (" other ") + ("tuples")
# > ("hello", " other ", "tuples")


# IIIb. DICTIONARIES are sequences of key-value pairs, and are denoted with curly brackets.

var_empty_dict_1 = {}
var_empty_dict_2 = dict()

var_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# You can retrieve values from a dictionary by using square brackets:
print(var_dict["key1"])
# > value1

# Note that the Dictionary data type is incredibly powerful and common in all
# languages by different names. In Python, it is called a `dictionary`, but it
# is very similar to `maps`, `hashmaps`, `associative arrays`, `objects`, etc.
# that are seen in other languages.
