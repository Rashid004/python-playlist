name = "Rashid"

print(id(name))

name = "Ansari"

print(id(name))


# Mutable data types
numbers = [1, 2, 3]

print(id(numbers))

numbers.append(4)

print(id(numbers))

a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(a is b)