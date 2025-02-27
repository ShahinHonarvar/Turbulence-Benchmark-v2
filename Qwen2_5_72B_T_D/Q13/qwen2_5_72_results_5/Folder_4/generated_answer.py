def find_second_largest_num(numbers):
    subset = numbers[12:93]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    second_max = float('-inf')
    for num in subset:
        if max_num > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None