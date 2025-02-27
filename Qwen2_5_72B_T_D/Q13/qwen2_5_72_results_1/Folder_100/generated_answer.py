def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[42:69]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset), reverse=True)[1]