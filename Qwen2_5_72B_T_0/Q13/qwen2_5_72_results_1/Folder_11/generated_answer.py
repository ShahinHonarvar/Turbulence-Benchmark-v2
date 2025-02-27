def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[37:52]
    subset.remove(max(subset))
    return max(subset) if subset else None