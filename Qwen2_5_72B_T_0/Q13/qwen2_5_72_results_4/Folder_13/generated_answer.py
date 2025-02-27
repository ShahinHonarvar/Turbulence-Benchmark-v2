def find_second_largest_num(numbers):
    if len(numbers) < 88 or len(set(numbers)) != len(numbers):
        return None
    subset = numbers[25:88]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)