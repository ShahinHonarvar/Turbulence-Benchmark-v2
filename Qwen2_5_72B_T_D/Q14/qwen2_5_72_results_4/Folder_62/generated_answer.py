def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = numbers[10:67]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]