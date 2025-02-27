def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    sublist = numbers[:11]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]