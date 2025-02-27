def find_second_smallest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 56:
        return None
    subset = numbers[55:99]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]