def find_second_largest_num(numbers):
    subset = numbers[20:201]
    if len(subset) < 2:
        return None
    unique_sorted_subset = sorted(set(subset), reverse=True)
    if len(unique_sorted_subset) < 2:
        return None
    return unique_sorted_subset[1]