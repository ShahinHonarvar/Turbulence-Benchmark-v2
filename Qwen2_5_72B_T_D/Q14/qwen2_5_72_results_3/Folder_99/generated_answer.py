def find_second_smallest_num(numbers):
    if len(numbers) < 609:
        return None
    subset = numbers[608:610]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if subset[0] != subset[1] else None