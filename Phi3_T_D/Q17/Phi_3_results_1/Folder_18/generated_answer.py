def all_ints_div_by_both_two_nums(numbers):
    start, end = (55, 66)
    return [num for num in numbers[start:end + 1] if num % 22 == 0 and num % 82 == 0]