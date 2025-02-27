def find_second_largest_num(numbers):
    start, end = (31, 72)
    sliced_nums = numbers[start:end + 1]
    if len(sliced_nums) < 2:
        return None
    first_largest, second_largest = sorted([max(sliced_nums), min(sliced_nums)])[::-1]
    for num in sliced_nums:
        if num > first_largest:
            second_largest, first_largest = (first_largest, num)
        elif num < first_largest and num > second_largest:
            second_largest = num
    return second_largest