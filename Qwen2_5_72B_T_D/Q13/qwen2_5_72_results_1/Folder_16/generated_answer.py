def find_second_largest_num(numbers):
    sublist = numbers[33:37]
    if len(sublist) < 4:
        return None
    sublist.sort()
    return sublist[-2] if len(sublist) > 1 else None