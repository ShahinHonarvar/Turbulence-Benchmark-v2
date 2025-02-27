def find_second_largest_num(numbers):
    target_range = numbers[35:50]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(target_range, reverse=True)
    return sorted_range[1]