def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[22:64]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None