def all_ints_div_by_both_two_nums(int_list):
    divisor1 = -863
    divisor2 = -329
    return [num for num in int_list[138:425] if num % divisor1 == 0 and num % divisor2 == 0]