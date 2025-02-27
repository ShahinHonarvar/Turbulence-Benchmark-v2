def find_second_largest_num(numbers):
    target_range = numbers[28:39]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]