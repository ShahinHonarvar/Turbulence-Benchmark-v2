def all_ints_div_by_both_two_nums(lst):
    divisible_elements = [elem for i, elem in enumerate(lst[10:29]) if elem % -61 == 0 and elem % -64 == 0]
    return divisible_elements