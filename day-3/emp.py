class Employee:
    def __init__(self,fname,lname,address):
        self.firstname=fname
        self.lastname=lname
        self.address=address
    def getFullname(self):
        return self.firstname+' '+self.lastname+' '+self.address

m1=Employee('vh','gyhb','ggbv')
fu=m1.getFullname()
print(fu)
