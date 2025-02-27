def find_second_largest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    subset = numbers[19:93]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)