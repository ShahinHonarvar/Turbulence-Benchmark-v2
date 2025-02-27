def find_second_smallest_num(numbers):
    if len(numbers) < 88 or len(set(numbers)) != len(numbers):
        return None
    sublist = numbers[30:88]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None