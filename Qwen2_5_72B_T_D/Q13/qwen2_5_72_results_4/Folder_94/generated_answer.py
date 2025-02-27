def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    subset = numbers[28:41]
    subset.sort(reverse=True)
    if len(subset) <= 1:
        return None
    return subset[1]