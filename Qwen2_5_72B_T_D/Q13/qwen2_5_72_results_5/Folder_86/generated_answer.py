def find_second_largest_num(numbers):
    sublist = numbers[31:35]
    if len(sublist) < 4:
        return None
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]