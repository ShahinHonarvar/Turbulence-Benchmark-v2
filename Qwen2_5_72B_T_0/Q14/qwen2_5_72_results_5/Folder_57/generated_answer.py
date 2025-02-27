def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    subset = numbers[20:31]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]