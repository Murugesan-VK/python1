class data:
    def __init__ (self,name,reg_number,total_fees,fees_paid,fee_balance):
        self.Name=name
        self.Reg_number=reg_number
        self.Total_fees=total_fees
        self.Fees_paid=fees_paid
        self.Fee_balance(total_fees-fees_paid)==fee_balance
class acc_1(data):
    def NAME(self):
        return f"name:{self.Name}"
    def REG_number(self):
        return f"Reg_number:{self.Reg_number}"
    def TOTAL_fees(self):
        return f"Total_fees:{self.Total_fees}"
    def FEES_paid(self):
        return f"Fees paid:{self.Fees_paid}"
    def FEE_balance(self):
        return f"Fee balance:{self.Fee_balance(total_fees-fees_paid)}"
class acc_2(data):
    def NAME(self):
        return f"name:{self.Name}"
    def REG_number(self):
        return f"REG_number:{self.Reg_number}"
    def TOTAL_fees(self):
        return f"Total_fees:{self.Total_fees}"
    def FEES_paid(self):
        return f"Fees paid:{self.Fees_paid}"
    def FEE_balance(self):
        return f"Fee balance:{self.Fee_balance(total_fees-fees_paid)}"
Acc_1=acc_1("daniel","930756","50000","65800")
Acc_2=acc_2("kavi","632580","078058","605865")

print(Acc_1.NAME())
print(Acc_1.REG_number())
print(Acc_1.TOTAL_fees())
print(Acc_1.FEES_paid())
print(Acc_1.FEE_balance())
print(Acc_2.NAME())
print(Acc_2.REG_number())
print(Acc_2.TOTAL_fees())
print(Acc_2.FEES_paid())
print(Acc_2.FEE_balance())
