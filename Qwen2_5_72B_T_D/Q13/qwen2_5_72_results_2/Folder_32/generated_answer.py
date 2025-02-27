def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 22:
        return None
    subset = numbers[21:98]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]