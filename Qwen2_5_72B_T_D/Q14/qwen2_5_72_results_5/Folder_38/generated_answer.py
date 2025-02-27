def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 37:
        return None
    subset = numbers[37:52]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]