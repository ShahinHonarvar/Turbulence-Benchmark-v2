def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    subset = numbers[23:24]
    if len(subset) == 1:
        return None
    return sorted(subset)[-2]