
#print(range(5))

#print(list(range(5)))

#print(list(range(1, 10, 2)))

for number in range(5):
       print(number)

print("-----------------")

a_dict = {"one":1, "two":2, "three":3}
keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
       print(key)

print("-----------------")

for number in range(10):
        if number % 2 == 0:
            print(number)

print("-----------------")          
i = 0
while i < 10:
        print(i)
        if i == 5:
            break
        i += 1


print("-----------------")

i = 0

while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1


print("-----------------")

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")