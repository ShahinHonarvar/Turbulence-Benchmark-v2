def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sliced_nums = numbers[42:69]
    if len(set(sliced_nums)) < 2:
        return None
    largest = max(sliced_nums)
    second_largest = None
    for num in sliced_nums:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest