def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[6:7]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]