def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    subset = numbers[56:83]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset), reverse=True)[1]