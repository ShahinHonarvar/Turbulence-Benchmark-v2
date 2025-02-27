def all_ints_div_by_both_two_nums(lst):
    divisors = [-33, -62]
    returned_int_list = [num for num in lst[80:86] if all((num % divisor == 0 for divisor in divisors))]
    return returned_int_list