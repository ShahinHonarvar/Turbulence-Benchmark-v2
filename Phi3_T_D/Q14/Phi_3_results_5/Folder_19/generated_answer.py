def find_second_smallest_num(numbers):
    target_range = numbers[4:9]
    unique_elements = sorted(set(target_range))
    return unique_elements[1] if len(unique_elements) > 1 else None