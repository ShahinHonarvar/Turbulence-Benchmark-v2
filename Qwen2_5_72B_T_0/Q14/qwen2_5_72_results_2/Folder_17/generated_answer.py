def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    subset = numbers[28:39]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]