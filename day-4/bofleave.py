from leave import leave
class BasketOfLeave(leave):
    def _init_(self, Employeeid, Name, LeaveBalance, Applyingleave):
        super()._init_(Employeeid,Name,LeaveBalance)
        self.Applyingleave=Applyingleave

    def displayleave(self):
        return self.LeaveBalance-self.Applyingleave
