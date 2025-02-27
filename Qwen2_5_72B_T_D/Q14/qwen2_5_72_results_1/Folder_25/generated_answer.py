def find_second_smallest_num(numbers):
    if len(numbers) < 77 or len(numbers) < 38:
        return None
    subset = numbers[37:77]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]