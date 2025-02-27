def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 22:
        return None
    subset = numbers[21:98]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None