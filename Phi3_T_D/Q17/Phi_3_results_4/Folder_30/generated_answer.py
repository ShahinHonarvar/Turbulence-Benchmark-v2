def all_ints_div_by_both_two_nums(integers):
    divisor1, divisor2 = (-81, -94)
    return [integer for integer in integers[11:77] if integer % divisor1 == 0 and integer % divisor2 == 0]