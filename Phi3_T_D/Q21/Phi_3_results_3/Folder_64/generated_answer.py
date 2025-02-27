def all_ints_div_by_num(int_list):
    if not isinstance(int_list, list) or not all((isinstance(x, int) for x in int_list)):
        raise ValueError('Argument must be a list of integers.')
    divisible_by_4 = [x for x in int_list[0:1] if x % 4 == 0]
    return divisible_by_4