def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[37:52]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)