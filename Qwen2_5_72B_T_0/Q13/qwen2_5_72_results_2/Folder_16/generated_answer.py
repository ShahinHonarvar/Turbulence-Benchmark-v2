def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    subset = numbers[33:37]
    subset.remove(max(subset))
    return max(subset) if subset else None