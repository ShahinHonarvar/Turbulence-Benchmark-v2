def all_ints_not_div_by_num(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 15 and i < 63 and (num % 34 != 0)]