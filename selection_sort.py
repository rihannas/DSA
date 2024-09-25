def selection_sort(list):
    for i in  range(len(list)):
        min = i
        for j in  range(i+1, len(list)):
            if list[j] < list[min]:
                print(min)
                min = j
        list[i], list[min] = list[min], list[i]

    return list

# i need to use idx, b/c that's how i will 
# i need to somehow shrink the list


print(selection_sort([6, 9, 2, 1, 5]))