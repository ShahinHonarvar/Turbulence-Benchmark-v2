def all_ints_div_by_both_two_nums(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 81 and i <= 86 and (num % -33 == 0) and (num % -62 == 0):
            result.append(num)
    return result