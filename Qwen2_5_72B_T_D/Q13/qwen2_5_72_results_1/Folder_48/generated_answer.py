def find_second_largest_num(numbers):
    if len(numbers) < 606 or len(numbers) <= 533:
        return None
    subset = numbers[533:606]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None