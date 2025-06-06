def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    subset = numbers[12:93]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None