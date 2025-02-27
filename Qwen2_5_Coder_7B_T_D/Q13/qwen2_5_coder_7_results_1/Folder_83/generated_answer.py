def find_second_largest_num(numbers):
    if len(numbers) < 101:
        return None
    subset = numbers[90:91]
    if len(subset) < 2:
        return None
    return sorted(subset)[-2]