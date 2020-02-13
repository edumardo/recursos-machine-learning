# Lists: mutables & []

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [				# List of lists
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]

mix = [32, 'hello']     # Lists can contain a mix of different types

planets[0]              # Mercury
planets[-1]             # Neptune
planets[-2]             # Uranus

planets[0:3]            # ['Mercury', 'Venus', 'Earth']
planets[:3]             # ['Mercury', 'Venus', 'Earth']
planets[3:]             # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[1:-1]           # All the planets except the first and last ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
planets[-3:]            # The last 3 planets ['Saturn', 'Uranus', 'Neptune']

planets[3] = 'Malacandra'								# Lists are mutables!
planets[:3] = ['Mur', 'Vee', 'Ur']						# Multiple assign
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]    # ['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

len(planets)            # Length of a list
sorted(planets)         # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

primes = [2, 3, 5, 7]
sum(primes)             # 17
max(primes)             # 7
int(123).bit_length()   # Number of bits necessary to represent self in binary: 7

planets.append('Pluto') # Append to the end
planets.pop()           # Removes and return the last element of a list

planets.index('Earth')  # Index of an element -> bad practices!
'Earth' in planets      # Returns boolean

# Tuples: inmutables & ()

t = (1, 2, 3)
t = 1, 2, 3             # equivalent to above

t[0] = 100              # Tuples are inmutables!

float(0.125).as_integer_ratio()                         # Some functions return tuples: (1, 8)
numerator, denominator = x.as_integer_ratio()           # Multiple return values can be individually assigned
