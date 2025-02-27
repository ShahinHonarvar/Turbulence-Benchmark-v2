def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[63:67]
    subset.sort()
    return subset[1] if len(subset) > 1 else None