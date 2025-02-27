def find_second_smallest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    subset.remove(min(subset))
    return min(subset) if subset else None