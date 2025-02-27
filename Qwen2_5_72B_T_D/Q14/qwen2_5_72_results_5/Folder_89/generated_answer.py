def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[62:64]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]