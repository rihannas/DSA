def quicksort(list):

    if len(list) < 2:
        return list

    pivot = list[len(list)//2]
    lesser = []
    greater = []
    
    for num in list:
        if pivot < num:
            greater.append(num)
        elif pivot > num :
            lesser.append(num)
    return quicksort(lesser) + [pivot] + quicksort(greater)


print(quicksort([6, 9, 2, 1, 5]))