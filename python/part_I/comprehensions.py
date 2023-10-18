x = [i for i in range(5)]


line = "This is the end of the line ."
if [i for i in line if "." in i]:
    print("Found it!")
else:
    print("Nope, not there!")

print("-----------------")

x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]

print(y)

print("-----------------")

print([i for i in range(10) if i % 2 == 0])

print("-----------------")

my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
my_set2 = {x for x in my_list}
print(my_set)
print(my_set2)


#List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]


#Tuple Comprehensions
numbers = (1, 2, 3, 4, 5)
squares = tuple(x**2 for x in numbers)

#Dictionary Comprehensions 
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
