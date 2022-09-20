"""

real    0m8.837s
user    0m6.996s
sys     0m1.840s
"""

#build a list of animals
#animals = ['cat', 'dog', 'monkey']

#build a regular for loop
#for animal in animals:
#    print(animal)

#build a list comprehension version
#[print(animal) for animal in animals]

#build a list of random numbers from 0 to 1 million
numbers = [x for x in range(100000000)]

#profile the time it takes to run the for loop
#build a regular for loop
# unoptimzed to 14 seconds
#collect = []
#for number in numbers:
#    collect.append(number)

#build a list comprehension version
# optimized to 0.5 seconds
collect = [number for number in numbers]




