def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sublist = numbers[62:100]
    sublist.sort()
    if len(sublist) <= 1:
        return None
    return sublist[-2]