def find_second_smallest_num(numbers):
    valid_range = numbers[10:101]
    if len(valid_range) < 2:
        return None
    sorted_range = sorted(valid_range)
    return sorted_range[1]