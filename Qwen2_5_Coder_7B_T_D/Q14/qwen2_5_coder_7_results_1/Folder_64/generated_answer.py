def find_second_smallest_num(numbers):
    if len(numbers) <= 4:
        return None
    subset = numbers[:5]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]