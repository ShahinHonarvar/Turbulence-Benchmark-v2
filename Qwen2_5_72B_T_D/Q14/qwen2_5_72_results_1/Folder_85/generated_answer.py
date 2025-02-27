def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[:7]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None