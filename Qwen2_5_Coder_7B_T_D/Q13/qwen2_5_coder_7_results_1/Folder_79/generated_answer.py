def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[4:5]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1]