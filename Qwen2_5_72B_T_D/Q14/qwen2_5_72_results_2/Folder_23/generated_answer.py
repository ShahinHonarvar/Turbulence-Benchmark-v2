def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(set(numbers[19:93])) < 2:
        return None
    subset = sorted(numbers[19:93])
    return subset[1]