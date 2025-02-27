def find_second_smallest_num(numbers):
    target_range = numbers[75:85 + 1]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[1]