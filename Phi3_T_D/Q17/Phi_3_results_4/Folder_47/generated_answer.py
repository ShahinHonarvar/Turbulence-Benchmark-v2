def all_ints_div_by_both_two_nums(numbers):
    start, end = (42, 87)
    return [num for num in numbers[start:end + 1] if num % -90 == 0 and num % -74 == 0]