# 4.2 Write a recursive function to count the number of items in a list.
def recursive_counter(list):
    if list == []:
        return 0
    return 1 + recursive_counter(list[1:])

print(recursive_counter([1, 4, 5, 8, 67, 294, 0, 3])) #8