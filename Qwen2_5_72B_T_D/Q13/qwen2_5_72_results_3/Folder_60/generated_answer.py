def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    subset = numbers[75:86]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort()
    if len(unique_subset) < 2:
        return None
    return unique_subset[-2]