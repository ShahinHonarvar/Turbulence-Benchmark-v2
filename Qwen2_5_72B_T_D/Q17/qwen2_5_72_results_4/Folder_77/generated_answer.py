def all_ints_div_by_both_two_nums(lst):
    divisor_1 = -649
    divisor_2 = -461
    start_index = 828
    end_index = 932
    result = [num for num in lst[start_index:end_index + 1] if num % divisor_1 == 0 and num % divisor_2 == 0]
    return result