# 4.1 Write out the code for the earlier sum function.
def recursive_sum(list):
  if len(list) == 0:
    return 0
  return list[0] + recursive_sum(list[1:])


print(recursive_sum([1, 4, 5, 8, 67, 294, 0, 3])) #382