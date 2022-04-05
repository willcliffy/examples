"""
Week 1 exercise hints

1. use the `in` keyword. This can be done in 1 line.

2. use a `for` loop. This can be done in 1 line, but you might want to do it in 5-6 lines

3. use array slicing. This can be done in 1 line.

4. This one is purposefully tricky. Play around with it a little longer.
   If you're confused what I'm asking for, send a text.

   Still stuck? This can be done in 4 lines.
   - you should have a while loop with the condition `n > 0`.
   - inside that while loop, you should call `n -= 1` and `print(n)`
   - after the loop, you should `return n`

5. This can be done in two lines. Use the built in "append" function to add the item to the list
   There are two common ways to check if a dictionary contains a key:
"""

key = "a key"
dict = {
   key: ["value"]
}

if key in dict:
    print("dict contains key:", key)

if dict.has_key(key):
    print("dict contains key:", key)
