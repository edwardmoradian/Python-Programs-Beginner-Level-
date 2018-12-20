# Author:  Edward Moradian

def ReadFile2():
    File = open("numbers2.txt","r")
    Numbers = File.readlines()
    
    i = 0
    while i < len((Numbers)):
        Numbers[i] = Numbers[i].rstrip("\n")
        i += 1
  
    File.close()
    print(Numbers)
    print("There are",len(Numbers),"rows in the matrix.")    
    return Numbers

def UserInput():
    RowNum = int(input("Please indicate the row number to view in the matrix:"))
    RowNum -= 1
    
    return RowNum

def DisplayAns(RowNum, List):
    print(List[RowNum])

def Main():
    Numbers = ReadFile2()
    RowNum = UserInput()
    Display = DisplayAns(RowNum, Numbers)
    
Main()