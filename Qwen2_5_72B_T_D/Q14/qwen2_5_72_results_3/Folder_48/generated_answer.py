def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 751:
        return None
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    unique_sorted_subset = sorted(set(subset))
    if len(unique_sorted_subset) < 2:
        return None
    return unique_sorted_subset[1]