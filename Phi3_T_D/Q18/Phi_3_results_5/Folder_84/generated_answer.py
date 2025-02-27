def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[78:82] if i % 76 == 0 or i % 60 == 0))