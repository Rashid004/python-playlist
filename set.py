# s1 = {}

# print(type(s1))


s1 = {1,2,3,4,5}
print(s1)

s2 = {1,1,2,2,2,3,4,5}
print(s2)

s3 = ([1,2], "Hello", 3.14, True)
print(s3)

s4 = set("Hello World")
print(s4)

s5 = set([1,2,3,4,5])
print(s5)

s6 = set((1,2,3,4,5))
print(s6)

s7 = set({1: "one", 2: "two", 3: "three"})
print(s7)

s6.add(6)
print(s6)

s6.remove(3)
print(s6)

s6.discard(4)
print(s6)

for i in s6:
    print(i)