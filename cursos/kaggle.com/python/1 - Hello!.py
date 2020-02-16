# Hello, Python!

spam_amount = 0             # We dont need to tell Python what type of value is going to refer to
spam_amount = 'Hello'       # We can even go on to reassign to refer to a different sort of thing like a string or a boolean
viking_song = "Spam " * 4   # Spam Spam Spam Spam

# Numbers and arithmetic in Python

type(spam_amount)           # what kind of thing is this?: int
type(19.95)                 # double

print(5 / 2)                # 2.5
print(5 // 2)               # // operator gives us a result that's rounded down to the next integer: 2

# Builtin functions for working with numbers

min(1, 2, 3)
max(1, 2, 3)
abs(-123)

print(float(10))            # 10.0
print(int(3.33))            # 3
print(int('807') + 1)       # 808
