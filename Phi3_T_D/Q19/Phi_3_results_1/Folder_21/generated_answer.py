def all_ints_not_div_by_num(integers):
    start_index = 469
    end_index = 566
    return [val for val in integers[start_index:end_index] if val % -692 != 0]