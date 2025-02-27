def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    sublist = numbers[19:93]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]