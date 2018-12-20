# Author:  Edward Moradian
# Create Rows of Asteriks

RowsNum = input("Please enter the number of rows: ")
RowsNum = int(RowsNum)

while (RowsNum < 0):
    print("Number of rows must be positive.")
    RowsNum = input("Please enter the number of rows: ")
    RowsNum = int(RowsNum)
    
i = 0
j = 0

for i in range(RowsNum):
    i += 1
    for j in range(RowsNum):
        print("*", end="")
    print("")
    RowsNum -= 1