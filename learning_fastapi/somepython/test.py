import sys

a = [1, 2, 3, 4, 5,6]
print("Initial reference count for object 'a':", sys.getrefcount(a))
sys.getrefcount(a)
b = a  # Now both 'a' and 'b' refer to the same list
print("Reference count after assigning 'b = a':", sys.getrefcount(a))

c = a  # Another reference
print("Reference count after assigning 'c = a':", sys.getrefcount(a))

del b  # Remove one reference
print("Reference count after 'del b':", sys.getrefcount(a))

del c  # Remove another reference
print("Reference count after 'del c':", sys.getrefcount(a))
