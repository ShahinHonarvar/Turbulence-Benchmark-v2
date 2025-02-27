def all_ints_not_div_by_num(lst):
    result = [elem for i, elem in enumerate(lst[469:566]) if elem % -692 != 0]
    return result