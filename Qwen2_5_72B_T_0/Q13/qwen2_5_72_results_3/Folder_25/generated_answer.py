def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    subset = numbers[29:94]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)