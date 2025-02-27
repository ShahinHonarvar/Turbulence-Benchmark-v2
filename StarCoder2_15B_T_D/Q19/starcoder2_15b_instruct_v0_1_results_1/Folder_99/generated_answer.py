def all_ints_not_div_by_num(integers_list):
    return [integer for i, integer in enumerate(integers_list) if i >= 387 and i < 516 and (integer % 310 != 0)]