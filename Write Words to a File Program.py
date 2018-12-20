# Author:  Edward Moradian

def UserInput():
    InputNum = int(input("Please enter the number of words to write on a file: "))
    return InputNum

def WriteFile(InputNum):
    File = open("File.txt","w")
    for i in range(InputNum):
        WordInput = input("Please enter the word to be written to the file: ")
        WordInput = WordInput.rstrip("\n")
        File.write(WordInput + "\n")
        
    File.close()
    
def main():
    InputNum = UserInput()
    File = WriteFile(InputNum)
    
main()