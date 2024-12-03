"""
Demonstrates:
Classes
Class Inheritance
"""

class Student:

	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def avemarks(self):
		return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):

	def __init__(self, name, school, salary):
		super().__init__(name, school)
		self.salary = salary

	def annualsalary(self):
		return  self.salary * 12

workingstudent1 = WorkingStudent('John', 'Aquinas', 30000)
workingstudent1.marks.append(81)
workingstudent1.marks.append(79)
workingstudent1.marks.append(91)
workingstudent1.marks.append(94)
print (f'{workingstudent1.name} from {workingstudent1.school} has an annual salary of {workingstudent1.annualsalary()} with an average grade of {workingstudent1.avemarks()}')