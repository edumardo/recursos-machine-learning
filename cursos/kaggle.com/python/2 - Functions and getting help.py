# Getting Help

help(print)     # Displays the header of that function and a brief description

# Defining functions

def myFunction(p1, p2):
    """
    This is the docstring and if we provide a function description,
    help() will show it.

    Good practice is to include one or more example calls.
    """
    # code and maybe a return

def myFunction(p1, p2 = 123)    # The function has one default argument
myFunction(1, 2)                # (1, 2)
myFunction(1)                   # (1, 123)
