def find_second_smallest_num(numbers):
    target_range = numbers[28:41]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(target_range)
    return sorted_range[1]