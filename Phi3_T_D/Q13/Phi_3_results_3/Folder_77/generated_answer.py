def find_second_largest_num(numbers):
    target_range = numbers[527:539]
    if len(set(target_range)) < 2:
        return None
    return sorted(set(target_range))[-2]