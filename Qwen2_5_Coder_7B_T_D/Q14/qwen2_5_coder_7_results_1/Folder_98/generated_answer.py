def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    subset = numbers[6:7]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]