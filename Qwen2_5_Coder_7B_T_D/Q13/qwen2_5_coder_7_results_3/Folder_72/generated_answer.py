def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[29:52]
    unique_subset = list(set(subset))
    if len(unique_subset) < 2:
        return None
    unique_subset.sort()
    return unique_subset[-2]