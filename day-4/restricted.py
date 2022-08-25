from leave import leave
class RestrictedLeave(leave):
    def _init_(self,Employeeid,Name,LeaveBalance,DateOfBirth):
        super()._init_(Employeeid,Name,LeaveBalance)
        self.dob=DateOfBirth
    def display_dob(self):
        return self.dob