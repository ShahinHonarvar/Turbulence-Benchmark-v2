def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    subset = numbers[52:72]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]