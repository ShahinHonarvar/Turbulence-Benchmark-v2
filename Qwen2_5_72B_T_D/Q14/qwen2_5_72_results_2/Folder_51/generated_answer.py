def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    subset = numbers[1:9]
    if len(set(subset)) < 2:
        return None
    return sorted(subset)[1]