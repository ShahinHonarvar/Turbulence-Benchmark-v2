def find_second_largest_num(numbers):
    target_range = numbers[50:55]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(set(target_range), reverse=True)
    return sorted_range[1] if len(sorted_range) > 1 else None