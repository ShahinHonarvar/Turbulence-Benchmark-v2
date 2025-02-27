def find_second_largest_num(numbers):
    if len(numbers) < 51 or len(numbers) < 23:
        return None
    subset = numbers[22:51]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None