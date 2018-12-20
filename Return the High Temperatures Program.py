# Author:  Edward Moradian


def GetTemps():
    Temperatures = [0] * 5
    Day = 1
    
    for i in range(5):
        print("Enter a temperature for day " + str(Day) + ": ",end="")
        Day = Day+1
        Temperatures[i] = float(input())
    return Temperatures
    
def FindHighTemperatures(Temperatures):
    HighTemperatures = []
    i=0
    length = len(Temperatures)
    
    for i in range(length):
        if Temperatures[i] >= 90.00:
            HighTemperatures.append(Temperatures[i])
            i+=1
        else:
            i+=1
            
    return HighTemperatures
    
def DisplayResults(HighTemperatures):
    length = len(HighTemperatures)
    print("\nTotal number of hot days: ",length)
    print("Your high temperatures for the week: ",end="")
    for i in range(length):
        print(str(HighTemperatures[i]),end=" ")

def main():
    Temperatures = GetTemps()
    HighTemperatures = FindHighTemperatures(Temperatures)
    DisplayResults(HighTemperatures)
    
main()