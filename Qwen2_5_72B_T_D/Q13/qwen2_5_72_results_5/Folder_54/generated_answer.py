def find_second_largest_num(numbers):
    subset = numbers[34:56]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort()
    if len(unique_subset) < 2:
        return None
    return unique_subset[-2]