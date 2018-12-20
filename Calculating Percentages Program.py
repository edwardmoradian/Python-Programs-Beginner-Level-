# Author:  Edward Moradian


NumMales = input("What is the number of males in the class? ")
NumMales = float(NumMales)

NumFemales = input("What is the number of females in the class? ")
NumFemales = float(NumFemales)

n = NumMales + NumFemales
PercentMales = NumMales/n
PercentFemales = NumFemales/n

print("The percent of males in the class are ",format(PercentMales,".2%"))
print("The percent of females in the class are ",format(PercentFemales,".2%"))