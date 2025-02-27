def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    subset = numbers[28:39]
    subset.remove(max(subset))
    return max(subset) if subset else None