def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    subset = numbers[:8]
    subset.remove(min(subset))
    return min(subset) if subset else None