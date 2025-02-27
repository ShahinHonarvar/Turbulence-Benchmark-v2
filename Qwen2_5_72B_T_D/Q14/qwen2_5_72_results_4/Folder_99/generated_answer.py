def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    subset = numbers[608:610]
    subset.sort()
    return subset[1] if len(subset) > 1 else None