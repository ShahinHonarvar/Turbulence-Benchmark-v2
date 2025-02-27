def find_second_largest_num(numbers):
    if len(numbers) < 53:
        return None
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None