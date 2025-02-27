def find_second_smallest_num(numbers):
    if len(numbers) < 37 or len(set(numbers)) != len(numbers):
        return None
    subset = numbers[33:37]
    subset.remove(min(subset))
    return min(subset) if subset else None