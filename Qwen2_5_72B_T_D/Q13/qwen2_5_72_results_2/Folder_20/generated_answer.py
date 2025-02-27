def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[56:67]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    second_largest = min(subset)
    for num in subset:
        if largest > num > second_largest:
            second_largest = num
    return second_largest