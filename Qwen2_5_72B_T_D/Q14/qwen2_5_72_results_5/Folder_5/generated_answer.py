def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    subset = numbers[3:6]
    subset.sort()
    return subset[1] if len(subset) > 1 else None