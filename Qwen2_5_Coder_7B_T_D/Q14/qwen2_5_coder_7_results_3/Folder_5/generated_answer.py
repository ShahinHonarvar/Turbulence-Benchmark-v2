def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    subset = numbers[3:6]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]