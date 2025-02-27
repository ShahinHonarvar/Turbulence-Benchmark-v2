def find_second_smallest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    subset = sorted(numbers[209:557])
    if len(subset) < 2:
        return None
    return subset[1]