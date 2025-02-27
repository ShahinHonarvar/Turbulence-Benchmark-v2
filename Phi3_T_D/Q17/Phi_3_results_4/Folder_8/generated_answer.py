def all_ints_div_by_both_two_nums(lst):
    divisor_lcm = -27 * -96 // math.gcd(-27, -96)
    return [x for x in lst[36:86:1] if x % divisor_lcm == 0]