# Author:  Edward Moradian

def UserInput():
    FileName = input("Please enter the file name: ")
    return FileName

def ReadFile(FileName):
    File = open(FileName,"r")
    line = File.readline()
    LineNum = 1
   
    while line != "":
        print("Line",LineNum,":\t",line,end="")
        line = File.readline()
        LineNum+=1

def main():
    FileName = UserInput()
    ReadFile(FileName)
    
main()