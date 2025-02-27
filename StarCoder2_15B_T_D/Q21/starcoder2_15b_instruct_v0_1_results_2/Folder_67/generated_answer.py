def all_ints_div_by_num(integers):
    return [integer for i, integer in enumerate(integers) if i >= 40 and i <= 68 and (integer % 16 == 0)]