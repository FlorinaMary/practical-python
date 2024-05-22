# there are 4 references to the list
a = [1, 2, 3]
b = a
c = [a, b]

# shalow copies

a = [2, 3, [100, 101], 4]
b = list(a)  # Make a copy
a is b  # False t’s a new list, but the list items are shared.

a = [2, 3, [100, 101], 4]
import copy

b = copy.deepcopy(a)
a[2].append(102)
b[2]  # [100,101]
a[2] is b[2]  # False


"""
Numbers, strings, lists, functions, exceptions, classes, instances, etc. are all objects. 
It means that all objects that can be named can be passed around as data, placed in containers, etc., without any restrictions. 
There are no special kinds of objects. Sometimes it is said that all objects are “first-class”.
"""
