def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 60:
        return None
    subset = numbers[59:98]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort()
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]