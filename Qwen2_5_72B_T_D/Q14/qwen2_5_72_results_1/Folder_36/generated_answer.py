def find_second_smallest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 209:
        return None
    sublist = numbers[209:557]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None