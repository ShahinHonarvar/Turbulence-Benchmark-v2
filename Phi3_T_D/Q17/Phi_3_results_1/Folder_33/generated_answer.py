def all_ints_div_by_both_two_nums(lst):
    divisor1, divisor2 = (-722, -731)
    start_index, end_index = (281, 694)
    return [num for num in lst[start_index:end_index + 1] if num % divisor1 == 0 and num % divisor2 == 0]