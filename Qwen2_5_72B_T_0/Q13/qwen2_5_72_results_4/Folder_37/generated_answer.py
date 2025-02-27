def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[1:6]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]