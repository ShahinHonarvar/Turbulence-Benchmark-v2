def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    subset = numbers[35:50]
    subset.remove(min(subset))
    if not subset:
        return None
    return min(subset)