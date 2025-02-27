def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[:2]
    sublist.sort()
    return sublist[0] if len(sublist) > 1 else None