def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list[154:799]) if num % 275 == 0 or num % 580 == 0))