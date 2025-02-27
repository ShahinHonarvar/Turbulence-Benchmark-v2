def sum_ints_div_by_either_nums(lst):
    return sum((el for i, el in enumerate(lst[68:100], start=68) if el % -37 == 0 or el % -26 == 0))