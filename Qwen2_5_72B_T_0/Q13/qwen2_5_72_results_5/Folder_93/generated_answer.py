def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    subset = numbers[75:95]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)