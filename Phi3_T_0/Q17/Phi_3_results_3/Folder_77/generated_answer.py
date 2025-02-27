def all_ints_div_by_both_two_nums(lst):
    divisor_product = -649 * -461
    return [x for x in lst[828:933] if x % divisor_product == 0]