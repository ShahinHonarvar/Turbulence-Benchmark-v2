def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    sublist = numbers[52:72]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]