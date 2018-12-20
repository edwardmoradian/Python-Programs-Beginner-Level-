# Author:  Edward Moradian

def UserInput():
    String = input("Please enter a string that you want properly capitalized:")
    return String

def Capitalize(String):
    Capital = String.capitalize()
    return Capital

def Main():
    String = UserInput()
    Capital = Capitalize(String)
    print(Capital)
    
Main()