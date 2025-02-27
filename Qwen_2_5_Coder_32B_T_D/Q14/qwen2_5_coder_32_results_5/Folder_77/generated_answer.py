def find_second_smallest_num(numbers):
    if len(numbers) < 976:
        return None
    sublist = numbers[639:976]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]