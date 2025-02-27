def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 101:
        return None
    subset = numbers[10:101]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]