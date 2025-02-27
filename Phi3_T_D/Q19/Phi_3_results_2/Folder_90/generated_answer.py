def all_ints_not_div_by_num(int_list):
    relevant_ints = int_list[767:905]
    return [num for num in relevant_ints if num % -430 != 0]