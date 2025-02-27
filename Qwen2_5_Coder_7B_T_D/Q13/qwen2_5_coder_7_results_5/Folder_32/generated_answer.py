def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    subset = numbers[21:98]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]