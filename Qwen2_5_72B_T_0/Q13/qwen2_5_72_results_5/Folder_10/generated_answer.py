def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    subset = numbers[25:60]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None