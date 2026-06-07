# String
str = input("Enter a string: ")
print("The string is: ", str)

# List
bool = input("Enter a boolean value (True/False): ")
if bool == "True":
    print("The boolean value is: True")
elif bool == "False": 
    print("The boolean value is: False")

else: 
   print("Invalid input. Please enter True or False.")


# Number
num = int(input("Enter a number: "))
print("The number is: ", num)

# float
flt = float(input("Enter a float number: "))
print("The float number is: ", flt)

# binary, octal, hexadecimal
bin_num = input("Enter a binary number: ")
oct_num = input("Enter an octal number: ")
hex_num = input("Enter a hexadecimal number: ")
print("The binary number is: ", bin_num)
print("The octal number is: ", oct_num)
print("The hexadecimal number is: ", hex_num)


# Array
arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = input("Enter element: ")
    arr.append(element)
print("The array is: ", arr)
