def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(len(integers)):
        if i >= 0 and i <= 1 and (integers[i] % -6 == 0) and (integers[i] % 4 == 0):
            result.append(integers[i])
    return result