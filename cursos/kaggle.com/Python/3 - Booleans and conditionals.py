# Booleans

True or False               # Type bool

3.0 == 3                    # True
'3' == 3                    # False

'A' and 'B' or 'C' not 'D'  # Combining boolean values
True or True and False      # and has a higer preference than or: True

# Boolean conversion
print(bool(1))              # All numbers are treated as true, except 0: True
print(bool(0))              # False
print(bool("asf"))          # All strings are treated as true, except the empty string ""
print(bool(""))             # False
                            # Generally empty sequences (strings, lists, tuples) are "falsey" and the rest are "truthy"

# Conditionals

if x == 0:
    print("x is zero")
elif x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("wtf?")

result = 'x is positive' if x > 0 else 'x is negative or zero'
    # Similar to the ternary operator
    # result = (x > 0) ? 'x is positive' : 'x is negative or zero'
