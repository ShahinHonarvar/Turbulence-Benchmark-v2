def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    subset = numbers[20:31]
    subset.remove(min(subset))
    return min(subset) if subset else None