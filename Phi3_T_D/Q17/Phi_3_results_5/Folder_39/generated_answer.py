def all_ints_div_by_both_two_nums(int_list):
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    divisor = gcd(-66, -32)
    return [i for i in int_list[13:77] if i % divisor == 0]