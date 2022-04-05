"""
EXERCISE 1 - variables, strings, arrays, functions

NOTE that none of these functions should be more than 10 lines.
If you find yourself writing really long functions, you've done something wrong.

For each exercise, write a function that...

1. takes two strings. Returns True if the second string is `in` the first string.

2. takes a string and a number `n`. Returns a list of that string with length `n`.

3. takes a string. Returns the first 3 characters of that string.
   Assume the string is 3 characters or longer.

4. takes a positive integer `n`.
   This function should have a while loop that runs while `n` is greater than 0.
   For each `iteration` of the loop, you should subtract 1 from `n` and print the current value of `n`.
   This function should return `n` after the loop completes.

5. takes a dictionary. Returns nothing.
   If the dictionary contains the key "backpack", then add the string "sword" to the backpack list.
   If the dictionary does not contain the key "backpack", do nothing.
   You can assume that if the dictionary has the key backback, that it's value is a list.

The first time you run this, it should look like this:
$ python3 Y1_exercise.py
FAIL exercise 1: 'world' should be in 'hello, world' but your function says that it is not.
FAIL exercise 2: expected return value to not be `None`
FAIL exercise 3: expected the first three characters of 'yesterday' to be 'yes' but got: None
FAIL exercise 4: expected n to equal 0 after funtion
FAIL exercise 5: expected sword to be in player 1's backpack: {'backpack': []}

When you get the following output, then you've done everything right:
$ python3 Y1_exercise.py
PASS exercise 1
PASS exercise 2
PASS exercise 3
2
1
0
PASS exercise 4
PASS exercise 5
"""


def exercise_1(string, substring):
    return None


def exercise_2(message, n):
    return None


def exercise_3(string):
    return None


def exercise_4(n):
    return None


def exercise_5(player):
    return None


# DON'T CHANGE THE CODE BELOW THIS POINT
if __name__ == "__main__":
    e1_result1 = exercise_1("hello, world", "world")
    e1_result2 = exercise_1("different", "strings")
    if not e1_result1:
        print("FAIL exercise 1: 'world' should be in 'hello, world' but your function says that it is not.")
    elif e1_result2:
        print("FAIL exercise 1: 'strings' should not be in `different`, but your function says that is is.")
    else:
        print("PASS exercise 1")

    e2_result1 = exercise_2("hello", 10)
    if e2_result1 is None:
        print("FAIL exercise 2: expected return value to not be `None`")
    elif len(e2_result1) != 10:
        print("FAIL exercise 2: expected the return of exercise_2('hello', 10) to have length 10")
    elif any([m != "hello" for m in e2_result1]):
        print("FAIL exercise 2: expected all the strings in the list to be 'hello', but got something else:", e2_result1)
    else:
        print("PASS exercise 2")

    e3_result1 = exercise_3("yesterday")
    e3_result2 = exercise_3("god damn")
    if e3_result1 != "yes":
        print("FAIL exercise 3: expected the first three characters of 'yesterday' to be 'yes' but got:", e3_result1)
    elif e3_result2 != "god":
        print("FAIL exercise 3: expected the first three characters of 'god damn' to be 'god' but got:", e3_result1)
    else:
        print("PASS exercise 3")

    e4_result1 = exercise_4(3)
    if e4_result1 != 0:
        print("FAIL exercise 4: expected n to equal 0 after funtion")
    else:
        print("PASS exercise 4")

    player1 = {"backpack": []}
    player2 = {"not a backpack": "nope"}
    player3 = {}

    exercise_5(player1)
    exercise_5(player2)
    exercise_5(player3)

    if "sword" not in player1["backpack"]:
        print("FAIL exercise 5: expected sword to be in player 1's backpack:", player1)
    elif "backpack" in player2 or "backpack" in player3:
        print("FAIL exercise 5: players 2 and 3 shouldn't have a backpack!")
    else:
        print("PASS exercise 5")
