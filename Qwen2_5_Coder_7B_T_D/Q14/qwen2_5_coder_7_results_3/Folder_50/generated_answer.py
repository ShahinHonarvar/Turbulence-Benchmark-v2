def find_second_smallest_num(numbers):
    subset = numbers[42:69]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]