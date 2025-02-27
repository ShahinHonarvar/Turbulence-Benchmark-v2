def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    subset = numbers[1:6]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]