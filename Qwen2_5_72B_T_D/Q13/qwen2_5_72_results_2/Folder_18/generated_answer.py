def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    subset = numbers[35:50]
    subset.remove(max(subset))
    if not subset:
        return None
    return max(subset)