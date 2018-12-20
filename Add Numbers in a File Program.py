# Author:  Edward Moradian

def AddInFile(File):
    total = 0.00
    line = File.readline()
    while line != "":
        line = float(line)
        total += line
        line = File.readline()
    return total
def main():
    File = open("numbers.txt","r")
    AddInFile(File)
    print(total)
    File.close()

main()