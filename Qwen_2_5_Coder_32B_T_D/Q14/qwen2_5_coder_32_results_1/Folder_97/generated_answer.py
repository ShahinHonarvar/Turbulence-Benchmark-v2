def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    sublist = numbers[31:35]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None