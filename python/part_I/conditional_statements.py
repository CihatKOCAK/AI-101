if 2 > 1:
        print("This is a True statement!")

var1 = 10
var2 = 20
if var1 > var2:
    print("This is also True")
else:
    print("That was False!")

x = 10
y = 20

if x < 10 or y > 15:
    print("This statement was True!")

my_list = [1, 2, 3, 4]
x = 10
z = 11
if x not in my_list and z != 10:
    print("This is True!")

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")