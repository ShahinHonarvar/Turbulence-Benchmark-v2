def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    subset = numbers[8:10]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]