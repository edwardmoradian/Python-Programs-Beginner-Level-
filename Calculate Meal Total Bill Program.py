# Author:  Edward Moradian


StringInput = input("Enter the amount you paid for your meal: ")
Charge = float(StringInput)

Tip = Charge * .18
SalesTax = Charge * .07
TotalBill = Charge + Tip + SalesTax

print("Tip: $" + format(Tip,".2f"))
print("Tax: $" + format(SalesTax,".2f"))
print("Total Bill: $" + format(TotalBill,".2f"))