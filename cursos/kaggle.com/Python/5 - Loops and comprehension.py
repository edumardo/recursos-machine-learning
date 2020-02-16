# Loops

list  = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
tuple = ('Earth', 'Mars')
str = 'Hello World'
for l in list:      # Any object tha supports iteration
for t int tuple:    # We can iterate over the elements of a tuple
for c in str:       # Even loop through each character in a string

for i in range(5):  # Range returns a sequence of numbers, [0, 4]
while i < 10:       # While loop

# List comprehensions

squares = [n**2 for n in range(10)]                                                     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
short_planets = [planet for planet in planets if len(planet) < 6]                       # ['Venus', 'Earth', 'Mars']
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]    # ['VENUS!', 'EARTH!', 'MARS!']
[32 for planet in planets]                                                              # [32, 32, 32, 32, 32, 32, 32, 32]

# Example: return the number of negative numbers in the given list
# Option 1: iteration
def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# Option 2: list comprehension
def count_negatives(nums):
    return ([num for num in nums if num < 0])

# Option 3: list comprehension + quirk of python (True + True + False + True to be equal to 3)
def count_negatives(nums):
    return sum([num < 0 for num in nums])
