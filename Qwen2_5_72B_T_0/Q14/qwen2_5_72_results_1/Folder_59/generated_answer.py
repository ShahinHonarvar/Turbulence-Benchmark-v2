def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    subset = numbers[:10]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]