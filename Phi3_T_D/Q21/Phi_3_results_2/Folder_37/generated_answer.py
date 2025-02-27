def all_ints_div_by_num(int_list):
    result = [num for i, num in enumerate(int_list[4:5]) if num % 3 == 0]
    return result