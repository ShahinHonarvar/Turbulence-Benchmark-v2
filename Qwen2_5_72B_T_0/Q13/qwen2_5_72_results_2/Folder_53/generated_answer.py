def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    subset = numbers[100:201]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None