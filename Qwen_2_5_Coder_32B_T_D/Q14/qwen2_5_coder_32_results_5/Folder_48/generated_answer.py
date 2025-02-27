def find_second_smallest_num(numbers):
    if len(numbers) < 751:
        return None
    sublist = sorted(numbers[246:751])
    if len(sublist) < 2:
        return None
    return sublist[1]