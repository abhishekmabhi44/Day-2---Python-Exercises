class student:
  def __init__(self,name,age,course):
    self.name= name
    self.age= age
    self.course= course
  def details(self):
    print("name=", self.name)
    print("age=", self.age)
    print("course=", self.course)
a1= student("Abhishek",2,"computer science") 
a1= details()
