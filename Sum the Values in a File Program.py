# Author:  Edward Moradian


def main():
    infile = open("numbers.txt", "r")
    line = infile.readline()
    amount = 0
    
    while line != "":
        number = float(line)
        amount += number
        line = infile.readline()
    
    infile.close()
    
    amount = format(amount, ".2f")
    print("The sum of the values in the file is: " ,amount)
    
main()