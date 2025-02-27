def find_second_largest_num(numbers):
    if not 20 <= len(numbers) >= 200:
        return None
    subset = numbers[20:201]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)