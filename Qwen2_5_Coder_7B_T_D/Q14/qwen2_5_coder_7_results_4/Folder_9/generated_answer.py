def find_second_smallest_num(numbers):
    subset = numbers[70:201]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]