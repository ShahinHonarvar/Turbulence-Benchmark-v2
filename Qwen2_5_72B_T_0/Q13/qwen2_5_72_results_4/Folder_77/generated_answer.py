def find_second_largest_num(numbers):
    if len(numbers) < 538:
        return None
    subset = numbers[527:539]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)