# Author:  Edward Moradian



TotalAmt = input("What is the total amount that you purchased? ")
TotalAmt = float(TotalAmt)

NumInstall = input("What is your desired number of installments? ")
NumInstall = int(NumInstall)

Tax = .05
TotalTax = TotalAmt * Tax
NetTotal = TotalAmt + TotalTax

InstallTotal = NetTotal/NumInstall

print("Your net total is ",NetTotal)
print("Your fee per installment is ",InstallTotal)