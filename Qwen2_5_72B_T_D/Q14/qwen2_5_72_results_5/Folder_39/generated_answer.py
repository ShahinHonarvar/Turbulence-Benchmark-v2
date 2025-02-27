def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    subset = numbers[28:41]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]