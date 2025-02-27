def all_ints_not_div_by_num(ints):
    return [num for i, num in enumerate(ints[3:9], start=3) if num % 6 != 0]