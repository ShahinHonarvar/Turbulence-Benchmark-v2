def sum_ints_div_by_either_nums(int_list):
    start_idx = 57
    end_idx = 85
    divisible_by_minus_77_or_32 = [num for num in int_list[start_idx:end_idx + 1] if num % -77 == 0 or num % -32 == 0]
    return sum(divisible_by_minus_77_or_32)