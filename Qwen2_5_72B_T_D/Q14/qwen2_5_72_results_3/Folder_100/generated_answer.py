def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[43:52]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]