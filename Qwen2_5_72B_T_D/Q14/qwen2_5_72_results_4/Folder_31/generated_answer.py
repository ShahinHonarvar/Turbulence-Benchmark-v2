def find_second_smallest_num(numbers):
    if len(numbers) < 94 or len(set(numbers[29:94])) < 2:
        return None
    sublist = sorted(numbers[29:94])
    return sublist[1]