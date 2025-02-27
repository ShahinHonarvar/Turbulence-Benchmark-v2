def all_ints_div_by_both_two_nums(lst):
    divisor_gcd = gcd(abs(-27), abs(-96))
    return [x for x in lst[36:86] if x % divisor_gcd == 0]