def sum_ints_div_by_either_nums(input_list):
    return sum((val for val in input_list[281:695] if val % -722 == 0 or val % -731 == 0))