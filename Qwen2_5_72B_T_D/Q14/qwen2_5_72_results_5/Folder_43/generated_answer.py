def find_second_smallest_num(numbers):
    if not 74 <= len(numbers) - 1 <= 95:
        return None
    subset = numbers[74:96]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]