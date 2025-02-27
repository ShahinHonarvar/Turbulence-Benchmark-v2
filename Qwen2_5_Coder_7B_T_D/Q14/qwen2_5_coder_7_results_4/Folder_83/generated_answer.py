def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    subset = numbers[90:201]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]