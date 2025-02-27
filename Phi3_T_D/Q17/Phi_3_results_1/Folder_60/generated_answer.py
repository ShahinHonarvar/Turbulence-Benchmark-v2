def all_ints_div_by_both_two_nums(lst):
    divisor1 = -74
    divisor2 = -58
    result = [num for num in lst[10:80] if num % divisor1 == 0 and num % divisor2 == 0]
    return result