def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    subset = numbers[5:8]
    if len(subset) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)