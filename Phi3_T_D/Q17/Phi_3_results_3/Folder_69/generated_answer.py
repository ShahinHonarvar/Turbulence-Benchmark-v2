def all_ints_div_by_both_two_nums(integers):
    divisible = [num for num in integers[61:89] if num % 31 == 0 and num % 11 == 0]
    return divisible