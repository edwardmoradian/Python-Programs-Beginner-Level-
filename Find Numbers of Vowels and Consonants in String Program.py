# Author:  Edward Moradian

def UserInput():
    String = input("Please enter a string: ")
    String = String.lower()
    return String

def VowelCal(String):
    Vowels = ["a","e","i","o","u"]
    j = 0
    NumVowels = 0
    for i in String:
        if i in Vowels:
            NumVowels += 1
     
    return NumVowels

def ConsCal(String,NumVowels):
    String = String.strip()
    String = String.strip(".")
    String = String.replace(" ","")
    LenString = len(String)
    NumCons = LenString - NumVowels
    
    return NumCons
    
def Main():
    String = UserInput()
    NumVowels = VowelCal(String)
    print("The number of vowels in the string is:",NumVowels)
    NumCons = ConsCal(String,NumVowels)
    print("The number of consonants in the string is:",NumCons)
    
Main()