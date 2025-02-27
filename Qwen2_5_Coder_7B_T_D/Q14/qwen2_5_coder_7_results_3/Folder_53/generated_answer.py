def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    subset = sorted(numbers[1:101])
    if len(set(subset)) < 2:
        return None
    return subset[1]