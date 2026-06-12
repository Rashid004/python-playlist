class Student:

      def __init__(self,fullName):
          self.name =  fullName
          print("adding new student in database..")


s1 = Student("Rashid")
s2 = Student("Sabrin")

print(s1.name)
print(s2.name)  