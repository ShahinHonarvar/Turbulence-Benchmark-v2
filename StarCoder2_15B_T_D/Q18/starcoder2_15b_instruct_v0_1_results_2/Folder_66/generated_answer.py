def sum_ints_div_by_either_nums(ints_list):
    filtered_ints = [i for i in ints_list[58:82] if i % 55 == 0 or i % 10 == 0]
    return sum(filtered_ints)