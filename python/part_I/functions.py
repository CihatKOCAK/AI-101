def a_function():
        print("You just created a function!")

a_function()

def add(a, b):
        return a + b

print(add(3, 5))

print("--------------------")

def keyword_function(a=1, b=2):
        return a+b

print(keyword_function(5))

print("--------------------")

def many(*args, **kwargs):
        print(args)
        print(kwargs)

many(1, 2, 3, name="Ali", job="Student")
