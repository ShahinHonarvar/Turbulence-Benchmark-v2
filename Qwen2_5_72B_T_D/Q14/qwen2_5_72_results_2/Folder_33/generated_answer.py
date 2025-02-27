def find_second_smallest_num(numbers):
    if len(numbers) < 747:
        return None
    subset = numbers[262:747]
    if len(subset) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)