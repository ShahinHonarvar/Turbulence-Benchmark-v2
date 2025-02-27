def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[:9]
    subset.sort()
    if len(set(subset)) < 2:
        return None
    return subset[1]