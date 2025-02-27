def sum_ints_div_by_either_nums(integers):
    divisors = [-649, -461]
    return sum((integer for integer in integers[828:933] if integer % divisors[0] == 0 or integer % divisors[1] == 0))