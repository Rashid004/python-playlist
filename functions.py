# def function_name():
#     print("Hello World")

# function_name()


# # def greet():
# #     print("Hello World")

# # greet()


# def greet(name):
#     print("Hello, " + name + "!")

# greet("Alice")
# greet("Rashid")


# def add(a,b):
#     return a + b

# result = add(5, 3)
# print("The sum is: ", result)

# def calculate_discount(price, discount):
#     discounted_price = (price * discount) / 100
#     return  price - discounted_price

# final_price = calculate_discount(1000, 20)

# print("The final price after discount is: ", final_price)

# def create_user(name,email):
#     user = {
#         "name": name,
#         "email": email
#     }
#     return user

# user = create_user("Rashid", "rashid@example.com")
# print(user)

def is_even(num):
    """This function checks if a number is even or not.
    Args:
        num (int): The number to check.
        Returns:
            bool: True if the number is even, False otherwise."""
    
    if num % 2 == 0:
        return print(num, "is an even number.")
    else:
        return print(num, "is an odd number.")
    
for i in range(1, 11):
    print(is_even(i))