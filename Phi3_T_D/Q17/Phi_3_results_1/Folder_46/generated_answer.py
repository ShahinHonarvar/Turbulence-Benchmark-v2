def all_ints_div_by_both_two_nums(int_list):
    start_index = 11
    end_index = 46
    divisors = (55, 36)
    divisible_ints = [num for num in int_list[start_index:end_index + 1] if all((num % divisor == 0 for divisor in divisors))]
    return divisible_ints