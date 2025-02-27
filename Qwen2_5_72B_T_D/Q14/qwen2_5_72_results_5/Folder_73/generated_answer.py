def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 60:
        return None
    subset = numbers[59:98]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]