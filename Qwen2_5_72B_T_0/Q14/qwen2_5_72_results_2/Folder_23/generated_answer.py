def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    subset = numbers[19:93]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]