def find_second_largest_num(numbers):
    subset = numbers[20:31]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if sorted_subset[0] != sorted_subset[1] else None