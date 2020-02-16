# Strings

x = 'Pluto is a planet'             # Single quotes
y = "Pluto is a planet"             # Double quotes
x == y                              # They are functionally equivalent: True

print("Pluto's a planet!")
print('My dog is named "Pluto"')
print('Pluto\'s a planet!')

hello = "hello\nworld"
triplequoted_hello = """hello
world"""
triplequoted_hello == hello         # True

# Strings are sequences

planet = 'pluto'
planet[0]                           # Indexing: p
planet[-3:]                         # Slicing: uto
len(planet)                         # 5
[char + '!' for char in planet]     # ['p! ', 'l! ', 'u! ', 't! ', 'o! ']

planet[0] = 'B'                     # Error! strings are inmutables!

# String methods

claim = "pluto is a planet!"
claim.upper()
claim.lower()
claim.index('plan')                 # 11
claim.startswith(planet)            # True
claim.endswith('dwarf planet')      # False

words = claim.split()               # String to list: ['Pluto', 'is', 'a', 'planet!']
d, m, y = '16/02/2020'.split('/')   # With separator
'-'.join([day, month, year])        # List to string, called string is the separator

'El nº ' + str(123) + ' está bien'  # Cast as string nonstrings variables
"El nº {} está bien".format(123)    # So much cleaner without cast!

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
    # 2 decimal points,3 decimal points format as percent, separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
    # "Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."

"El nº {0} está bien, aunque {1} es mayor que {0}".format(123, 456)

# Dictionaries (a built-in Python data structure for mapping keys to values)

numbers = {'one':1, 'two':2, 'three':3}
numbers['one']                                      # 1
number['eleven'] = 11                               # Adding another key,value pair
number['one'] = 'Pluto'

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
    # {'Mercury': 'M',
    # 'Venus': 'V',
    # 'Earth': 'E',
    # 'Mars': 'M',
    # 'Jupiter': 'J',
    # 'Saturn': 'S',
    # 'Uranus': 'U',
    # 'Neptune': 'N'}

'Saturn' in planet_to_initial                       # The in operator tells us whether something is a key in the dictionary: True
'Edu' in planet_to_initial                          # False

for k in numbers:                                   # A for loop over a dictionary will loop over its keys
    print('{} = {}'.format(k, numbers[k]))

' '.join(sorted(planet_to_initial.keys()))          # 'Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus'
' '.join(sorted(planet_to_initial.values()))        #' E J M M N S U V'

for planet, initial in planet_to_initial.items():   # items() method lets us iterate over the keys and values of a dictionary simultaneously
    print("{} begins with \"{}\"".format(planet, initial))
