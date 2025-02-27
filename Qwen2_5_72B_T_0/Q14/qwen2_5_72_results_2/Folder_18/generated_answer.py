def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    subset = numbers[30:49]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]