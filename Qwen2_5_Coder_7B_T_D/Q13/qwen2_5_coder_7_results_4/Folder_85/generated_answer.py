def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[6:9]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset))[-2]