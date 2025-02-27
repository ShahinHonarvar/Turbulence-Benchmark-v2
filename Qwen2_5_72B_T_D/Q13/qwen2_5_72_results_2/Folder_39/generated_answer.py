def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sublist = numbers[20:31]
    if len(set(sublist)) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    while sublist and sublist[-1] == largest:
        sublist.remove(largest)
    if not sublist:
        return None
    return max(sublist)