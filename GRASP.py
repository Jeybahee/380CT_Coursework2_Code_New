def quicksort(listToSort):
    less = []
    more = []
    equal = []
    if len (listToSort) > 1:
        pivot = listToSort[0]
        for i in listToSort:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                more.append(i)
        return quicksort(more)+equal+quicksort(less)
    else:
        return listToSort 
        
def graspSubsetSum(sortedList,tot):
    print("Sorted List: ",sortedList)
    current = 0
    used = []
    for i in range(len(sortedList)):
        if current < tot:
            current = current + sortedList[i]
            if current > tot:
                current = current - sortedList[i]
            else:
                used.append(sortedList[i])
        elif current == tot:
            return used
        else:
            return None

def localSearch(sortedList,greedyList,tot):
    print("")
    

List = [100,200,300,500,800,1000,10,50,90,70,30,5,9,1]
Total = 1207
print("Set: ", List)
print("Total: ", Total) 
sortedList = quicksort(List) 
out = graspSubsetSum(sortedList, Total)
print("Result: ", out)  
