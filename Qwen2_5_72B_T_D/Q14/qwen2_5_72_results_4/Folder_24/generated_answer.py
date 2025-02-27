def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    subset = [numbers[23]]
    if len(subset) < 2:
        return None
    first_min = min(subset)
    subset.remove(first_min)
    second_min = min(subset) if subset else None
    return second_min