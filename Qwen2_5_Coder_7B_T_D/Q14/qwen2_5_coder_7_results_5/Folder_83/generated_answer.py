def find_second_smallest_num(numbers):
    subset = numbers[90:201]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]