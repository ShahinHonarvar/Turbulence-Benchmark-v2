def all_ints_div_by_both_two_nums(ints):
    result = []
    divisor_product = -27 * -96
    for num in ints[36:86]:
        if num % divisor_product == 0:
            result.append(num)
    return result