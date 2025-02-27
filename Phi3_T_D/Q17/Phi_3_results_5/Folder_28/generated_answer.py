def all_ints_div_by_both_two_nums(lst):
    start = 34
    end = 81
    divisible_lst = [num for num in lst[start:end + 1] if num % 27 == 0 and num % 57 == 0]
    return divisible_lst