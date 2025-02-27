def find_second_largest_num(numbers):
    subset = numbers[34:56]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None