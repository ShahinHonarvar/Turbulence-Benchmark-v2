def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = sorted(numbers[:5])
    if len(set(subset)) < 2:
        return None
    return subset[1]