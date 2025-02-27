def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    sublist = numbers[30:49]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]