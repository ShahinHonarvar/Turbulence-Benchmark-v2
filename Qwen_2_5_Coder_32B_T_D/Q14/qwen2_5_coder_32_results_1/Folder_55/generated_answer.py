def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    sublist = numbers[10:11]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]