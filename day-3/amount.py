class account:
    def __int__(self,accountno,name,account_type,balance,amount):
        self.accountno=account_number
        self.name=name
        self.account_type=typeofaccount
        self.balance=balance
        self.amount=amount
    def withdraw(self):
        return self.accountno,self.name,self.account_type,self.balance,self.amount
        if(self.balance<self.amount):
            return'low balance'
        try:
            (self.balance<self.amount)
            raise 'low balance exception'
        except():
            pass
        else:
            return'sufficient amount'
        finally:
            print('exception handled')