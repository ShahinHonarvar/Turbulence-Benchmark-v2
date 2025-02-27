def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    subset = numbers[50:55]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort(reverse=True)
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]