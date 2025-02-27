def find_second_largest_num(numbers):
    subset = numbers[10:67]
    unique_subset = list(set(subset))
    if len(unique_subset) < 2:
        return None
    unique_subset.sort(reverse=True)
    return unique_subset[1]