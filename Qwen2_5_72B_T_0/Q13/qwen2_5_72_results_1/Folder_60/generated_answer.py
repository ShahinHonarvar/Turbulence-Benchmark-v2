def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    subset = numbers[75:86]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)