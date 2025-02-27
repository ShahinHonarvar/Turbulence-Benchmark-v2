def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)