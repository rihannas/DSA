def binary_search(list, target): 
    """Return the index of target"""
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        if guess  > target:  #could be an else statment
            high = mid - 1
    
    return None

my_list = [1, 3, 5, 7, 9, 11 , 34, 54]

print (binary_search(my_list, 34))