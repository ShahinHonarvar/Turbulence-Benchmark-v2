def all_ints_div_by_both_two_nums(integers):
    result = [integer for integer in integers[56:89] if integer % -59 == 0 and integer % -79 == 0]
    return result