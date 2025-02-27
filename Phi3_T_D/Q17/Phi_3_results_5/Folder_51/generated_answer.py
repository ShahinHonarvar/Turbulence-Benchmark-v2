def all_ints_div_by_both_two_nums(lst):
    divisible_by_neg_one_neg_ten = [num for num in lst[6:10] if num % -1 == 0 and num % -10 == 0]
    return divisible_by_neg_one_neg_ten