import sys
class Student:
    def __init__(self):
        self.studentname= ''
        self.studentnumber = 0
        self.contactnumber = 0
        self.IDnumber = 0
    def populate(self, n, m, l, o):
        self.studentname = n
        self.studentnumber = m
        self.contactnumber = l
        self.IDnumber = o
    def display(self):
        print("Student Name:", self.studentname)
        print("Student Number:", self.studentnumber)
        print("Contact Number:", self.contactnumber)
        print("ID Number:", self.IDnumber)

b=Student()

b.populate((str(input("Enter Student Name: "))), int(input("Enter Student Number: ")), int(input("Contact Number: ")), int(input("ID Number: ")))
print ("The student's name and their details are: ",)
b.display()