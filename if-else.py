email =  input("Apna Email Batao: ")
password = input("Apna Password Batao: ")

if email == "admin@example.com" and password == "admin123":
    print("Login successful!")
elif email == "admin@example.com" and password != "admin123":
    print("Incorrect password. Please try again.")
else: 
    print("Invalid email or password. Please try again.")