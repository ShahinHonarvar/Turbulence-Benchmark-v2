def find_second_smallest_num(numbers):
    if not 25 <= len(numbers) - 1 < 60:
        return None
    subset = numbers[25:60]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]