class student:
   def __init__(self,student_id,student_name):
      self.id=student_id
      self.name=student_name
   def Name(self):
      return self.id,self.name
emp1=student(2228,"sreenu")
m2=emp1.Name()
print(m2)