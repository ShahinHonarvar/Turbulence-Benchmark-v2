def all_ints_div_by_num(int_list):
    selected_range = int_list[31:73]
    divisible_by_63 = [num for num in selected_range if num % -63 == 0]
    return divisible_by_63