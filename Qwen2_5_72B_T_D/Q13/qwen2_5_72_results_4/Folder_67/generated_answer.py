def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    sublist = numbers[22:51]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    while sublist and max(sublist) == largest:
        sublist.remove(largest)
    if not sublist:
        return None
    return max(sublist)