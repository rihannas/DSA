def recursive_maxnum(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(recursive_maxnum([1, 4, 5, 8, 67, 294, 0, 3])) #294