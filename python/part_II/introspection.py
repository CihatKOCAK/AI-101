#type() Fonksiyonu
x = 5
print(type(x))  # <class 'int'>

#dir() Fonksiyonu
my_list = [1, 2, 3]
print(dir(my_list))

#help() Fonksiyonu
print(help(my_list.append))

#hasattr() Fonksiyonu
class Person:
    age = 23
    name = "Adam"

person = Person()

print('Person has age?:', hasattr(person, 'age'))

print('Person has salary?:', hasattr(person, 'salary'))

#example 2
my_dict = {"name": "Alice", "age": 30}
has_name = hasattr(my_dict, "name")
print(has_name)  # True


#getattr() ve setattr() Fonksiyonları: getattr() belirli bir niteliği almanıza ve setattr() belirli bir niteliği ayarlamanıza olanak tanır.

class SomeClass:
    attribute_name = "attribute_value"

my_object = SomeClass()
attribute_value = getattr(my_object, "attribute_name")
setattr(my_object, "new_attribute", "new_value")

#callable() Fonksiyonu
my_function = lambda x: x * 2
is_callable = callable(my_function)
