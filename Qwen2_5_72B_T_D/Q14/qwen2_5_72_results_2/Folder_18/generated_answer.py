def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    subset = numbers[30:49]
    subset.sort()
    return subset[1] if len(subset) > 1 else None