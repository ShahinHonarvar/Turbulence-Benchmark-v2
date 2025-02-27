def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    subset = numbers[23:24]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]