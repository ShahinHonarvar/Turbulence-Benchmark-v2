def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    subset = numbers[35:50]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)