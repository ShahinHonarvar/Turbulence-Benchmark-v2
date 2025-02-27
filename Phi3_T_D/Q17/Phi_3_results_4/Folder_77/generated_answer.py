def all_ints_div_by_both_two_nums(integers):
    divisible = [n for n in integers[828:932] if n % -649 == 0 and n % -461 == 0]
    return divisible