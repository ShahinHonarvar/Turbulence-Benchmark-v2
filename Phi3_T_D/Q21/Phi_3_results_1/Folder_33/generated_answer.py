def all_ints_div_by_num(int_list):
    if len(int_list) < 612:
        return []
    return [num for num in int_list[319:613] if num % -215 == 0]