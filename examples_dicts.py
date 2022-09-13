# create a dictionary full of fruits and their prices
fruits = {"apple": 1.00, "banana": 0.50, "orange": 0.75}

# print the price of an apple
print(fruits["apple"])

# find the price of the lowest priced fruit and print the price and the name of the fruit
lowest_price = min(fruits.values())
for fruit, price in fruits.items():
    if price == lowest_price:
        # use f-strings to print the name of the fruit and the price
        print(f"The lowest price is {price} and the fruit is {fruit}")

# add three more fruits to the dictionary along with their prices
fruits["pear"] = 0.25
fruits["grape"] = 0.75
fruits["pineapple"] = 2.00

# print the number of fruits in the dictionary
# print the number of fruits in the dictionary in a sentence
print(f"There are {len(fruits)} fruits and they are:")
for fruit in fruits:
    print(f"* {fruit} with the price of {fruits[fruit]}")

# create a dictionary full of unique md5 hashes and their corresponding file names
hashes = {
    "a1b2c3d4e5f6g7h8i9j0": "file1.txt",
    "b2c3d4e5f6g7h8i9j0a1": "file2.txt",
    "c3d4e5f6g7h8i9j0a1b2": "file3.txt",
}

# Big O Notation
# use (O1 lookup)
key1 = "b2c3d4e5f6g7h8i9j0a1"
key2 = "b2c3d4e5f6g7h8i9j0a3"
if key1 in hashes:
    print("yes")
if key2 in hashes:
    print("yes")

# use defaultdict
from collections import defaultdict

s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(sorted(d.items()))

# populate a dictionary with a list of keys and a list of values that has random integers as the values
import random

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
values = [random.randint(1, 100) for i in range(10)]
d = dict(zip(keys, values))
print(d)
# print values
print(d.values())

# use a counter to count the number of times a letter appears in a string
from collections import Counter

s = "this is a string"
c = Counter(s)
print(c)

# use a counter to count the number of fruits in a list
my_fruits = ["apple", "apple", "pear", "strawberry", "apple"]
c = Counter(my_fruits)
print(f"The following fruits are in the list: {c}")
