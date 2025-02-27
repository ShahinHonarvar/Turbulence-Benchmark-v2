def find_second_smallest_num(numbers):
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort()
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]