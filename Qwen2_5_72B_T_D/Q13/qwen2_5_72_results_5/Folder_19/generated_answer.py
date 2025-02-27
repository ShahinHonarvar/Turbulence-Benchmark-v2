def find_second_largest_num(numbers):
    sublist = numbers[3:6]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]