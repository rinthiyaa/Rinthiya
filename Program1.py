# Problem - 1
class calculater:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def caloperation(self,operation):
        if operation == "add":
            return self.a +self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a * self.b
        elif operation == "div":
            if self.b==0:
                return "Cannot divisible by Zero"
            else:
                return self.a / self.b
        else:
            return "Invalid Input"
a=float(input("Enter a number:"))
b=float(input("Enter a Number:"))
operation=input("Enter a operation (add,sub,mul,div):")
new=calculater(a,b)
output=new.caloperation(operation)
print("Result:",output)
