def function_name():
    print("Hello World")

function_name()


# def greet():
#     print("Hello World")

# greet()


def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Rashid")


def add(a,b):
    return a + b

result = add(5, 3)
print("The sum is: ", result)

def calculate_discount(price, discount):
    discounted_price = (price * discount) / 100
    return  price - discounted_price

final_price = calculate_discount(1000, 20)

print("The final price after discount is: ", final_price)