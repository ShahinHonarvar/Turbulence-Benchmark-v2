def all_ints_div_by_both_two_nums(numbers):
    divisor = 729
    start_idx, end_idx = (11, 76)
    return [num for num in numbers[start_idx:end_idx + 1] if num % divisor == 0]