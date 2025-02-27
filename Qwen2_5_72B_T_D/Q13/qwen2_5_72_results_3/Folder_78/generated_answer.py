def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[43:52]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]