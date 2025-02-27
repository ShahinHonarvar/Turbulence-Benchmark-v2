def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    subset = numbers[62:93]
    subset.remove(max(subset))
    return max(subset) if subset else None