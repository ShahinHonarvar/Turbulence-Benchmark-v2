def find_second_smallest_num(numbers):
    if len(numbers) < 557 or 209 > 556:
        return None
    sublist = numbers[209:557]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]