def all_ints_div_by_both_two_nums(integers):
    if len(integers) <= 584:
        raise ValueError('List must contain at least 585 items.')
    divisor_a = -553
    divisor_b = -737
    result = []
    for index in range(543, 585):
        if integers[index] % divisor_a == 0 and integers[index] % divisor_b == 0:
            result.append(integers[index])
    return result