def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    subset = numbers[52:72]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)