def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    subset = numbers[28:41]
    subset.remove(min(subset))
    return min(subset) if subset else None