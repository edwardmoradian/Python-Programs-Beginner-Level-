# Author:  Edward Moradian


def ReadFile():
        
    InFile = open("students.txt","r")
    Line = InFile.readline()
    WordList = Line.split(",")
    
    print("SID\tGPA")
    print("---\t---")
    
    GPA = []
    GPA.append(WordList[4].rstrip())
    
    print(WordList[0] +"\t"+ WordList[4],end="")
   
    while Line != "":
        Line = Line.strip()
        Line = InFile.readline()
        WordList = Line.split(",")
        if len(WordList)>1:
            GPA.append(WordList[4].rstrip())
            print(WordList[0] +"\t"+ WordList[4],end="")
        else:
            InFile.close()
            
    return GPA

def SumStats(GPA):
    
    GPA = list(map(float,GPA))
    
    MaxGPA = max(GPA)
    MinGPA = min(GPA)
    Total = 0
           
    for n in GPA:
        Total += n
        Average = Total/len(GPA)
    
    return MaxGPA, MinGPA, Average
    
def DisplayStats(MaxGPA, MinGPA, Average):
    print("\nAverage GPA is:\t",format(Average,".2f"))
    print("High GPA is:\t",format(MaxGPA,".2f"))
    print("Low GPA is:\t",format(MinGPA,".2f"))

def main():
    GPA = ReadFile()
    MaxGPA, MinGPA, Average = SumStats(GPA)
    DisplayStats(MaxGPA, MinGPA, Average)
    
main()