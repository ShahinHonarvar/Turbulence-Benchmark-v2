def find_second_smallest_num(numbers):
    if len(numbers) < 61:
        return None
    target_range = numbers[310:371]
    unique_values = sorted(set(target_range))
    if len(unique_values) < 2:
        return None
    return unique_values[1]