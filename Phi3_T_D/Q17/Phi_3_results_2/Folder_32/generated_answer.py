def all_ints_div_by_both_two_nums(int_list):
    quotient = None
    if len(int_list) >= 96:
        quotient = [(num for num in int_list[25:96] if num % 51 == 0 and num % 77 == 0)]
    return list(quotient) if quotient is not None else []