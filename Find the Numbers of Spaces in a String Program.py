# Author:  Edward Moradian

def MakeDictionary(List1,List2):
    Dict = {}
    j=0
    for i in List1:
        Dict[i] = List2[j]
        j+=1
    return Dict

def Main():
    List1 = [1,2,3,4]
    List2 = ["Red","Blue","Green","Yellow"]
    Dict = MakeDictionary(List1,List2)
    print(Dict)
    
Main()
