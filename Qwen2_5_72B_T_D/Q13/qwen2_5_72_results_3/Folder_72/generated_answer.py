def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 30:
        return None
    sublist = numbers[29:52]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None