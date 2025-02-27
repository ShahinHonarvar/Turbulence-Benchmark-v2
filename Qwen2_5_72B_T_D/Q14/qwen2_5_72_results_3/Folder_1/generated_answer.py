def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    subset = numbers[34:56]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]