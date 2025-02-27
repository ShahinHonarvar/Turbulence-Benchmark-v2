def all_ints_div_by_num(int_list):
    if len(int_list) <= 572 or len(int_list) <= 806:
        return []
    return [num for num in int_list[572:807] if num % -158 == 0]