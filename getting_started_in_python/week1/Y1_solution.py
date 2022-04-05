"""
EXERCISE 1 - variables, strings, arrays, functions

So that the output of this program is consistent, you will only be writing code inside of the functions below.

For each exercise, write a function that...

1. takes two strings
   returns True if the second string is `in` the first string

2. takes a string and a number `n`
   returns a list of that string with length `n`

3. takes a string
   returns the first 3 characters of that string
   Assume the string is 3 characters or longer

4. takes a positive integer `n`.
   This function should have a while loop that runs while `n` is greater than 0
   For each `iteration` of the loop, you should subtract 1 from `n` and print the current value of `n`
   This function should return `n` after the loop completes

5. takes a dictionary.
   If the dictionary contains the key "backpack", then add the string "sword" to the backpack list.
   If the dictionary does not contain the key "backpack", do nothing.
   You can assume that if the dictionary has the key backback, that it's value is a list.
"""


def exercise_1(string, substring):
    return substring in string


def exercise_2(message, n):
    return [message for _ in range(n)]


def exercise_3(string):
    return string[:3]


def exercise_4(n):
    while n > 0:
        n -= 1
        print(n)
    return n


def exercise_5(player):
    if "backpack" in player:
        player["backpack"].append("sword")


# don't modify code below this point
if __name__ == "__main__":
    e1_check1 = not exercise_1("hello, world", "world")
    e1_check2 = exercise_1("different", "strings")
    if e1_check1:
        print("FAIL exercise 1: 'world' should be in 'hello, world' but your function says that it is not.")
    elif e1_check2:
        print("FAIL exercise 1: 'strings' should not be in `different`, but your function says that is is.")
    else:
        print("PASS exercise 1")

    e2_result = exercise_2("hello", 10)
    e2_check1 = len(e2_result) != 10
    e2_check2 = any([m != "hello" for m in e2_result])
    if e2_check1:
        print("FAIL exercise 2: expected the return of exercise_2('hello', 10) to have length 10")
    elif e2_check2:
        print("FAIL exercise 2: expected all the strings in the list to be 'hello', but got something else:", e2_result)
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

    n = exercise_4(3)
    if n != 0:
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
