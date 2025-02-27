def find_second_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    subset = numbers[29:80]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]