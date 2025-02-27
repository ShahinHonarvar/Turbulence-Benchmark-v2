def sum_ints_div_by_either_nums(int_list):
    start, end = (86, 90)
    sum_divisible = sum((elt for elt in int_list[start:end + 1] if elt % -71 == 0 or elt % -67 == 0))
    return sum_divisible