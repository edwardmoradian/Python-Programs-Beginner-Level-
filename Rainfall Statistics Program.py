# Author:  Edward Moradian
# Calculate Rainfall Statistics

NumYears = input("Please give the number of years: ")
NumYears = int(NumYears)

while NumYears < 0:
    print("Negative years are not allowed please try again")
    NumYears = input("Please give the number of years: ")
    NumYears = int(NumYears)

Months = 12

Rainfall = 0.00
TotalRainfall = 0.00

i=0
j=0

for i in range(NumYears):
    i+=1
    for j in range(Months):
        Rainfall = input("Please give the inches of rainfall for a month: ")
        Rainfall = float(Rainfall)
        j+=1
        TotalRainfall += Rainfall 

TotalMonths = NumYears * Months
AverageRainfall = TotalRainfall/TotalMonths

print("\nMonths of total rain: ",TotalMonths)
print("Total rainfall: ",format(TotalRainfall,".3f"),"\"")
print("Average rainfall: ",format(AverageRainfall,".3f"),"\"")