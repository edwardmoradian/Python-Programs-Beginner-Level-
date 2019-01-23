
# Description of the Program: The program counts the number of distinct pairs in a list that add to a number.

def NumberOfPairs(ListOfNums,Kth):
    Count = 0
    StartIndex = 1
    
    for i in ListOfNums:
        for j in ListOfNums[StartIndex:]:
            if i+j == Kth:
                Count += 1
        StartIndex += 1
        
    return Count

def Main():
    ListOfNums = [0,1,2,3,4,5,1]
    Kth = 2
    Count = NumberOfPairs(ListOfNums,Kth)
    print(Count)
    
Main()