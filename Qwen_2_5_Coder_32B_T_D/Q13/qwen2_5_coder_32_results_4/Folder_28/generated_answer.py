def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[62:64]
    if len(sublist) < 2:
        return None
    first, second = (sublist[0], sublist[1]) if sublist[0] > sublist[1] else (sublist[1], sublist[0])
    return second