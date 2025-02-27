def find_second_smallest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    subset = numbers[660:925]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]