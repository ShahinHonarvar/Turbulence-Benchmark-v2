def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = numbers[28:33]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]