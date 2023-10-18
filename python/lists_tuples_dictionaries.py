my_list = []
my_list = list()

my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)
#print(combo_list)

my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2
#print(combo_list)

alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
#print(sorted_list)


# Tuples are immutable like a constant list
my_tuple = (1, 2, 3, 4, 5)
another_tuple = tuple()
abc = tuple([1, 2, 3])
abc_list = list(abc)

my_car = {
    "color": "red",
    "maker": "Toyota",
    "year": 2015
    }

print(my_car["color"])