def sum_ints_div_by_either_nums(numbers):
    start_idx = 315
    end_idx = 934
    divisor_one = -897
    divisor_two = -556
    return sum((num for i, num in enumerate(numbers[start_idx:end_idx + 1], start_idx) if num % divisor_one == 0 or num % divisor_two == 0))