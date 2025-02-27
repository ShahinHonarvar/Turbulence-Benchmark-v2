def sum_ints_div_by_either_nums(ints):
    ints_div_by_either_nums = []
    for i in range(len(ints)):
        if i >= 90 and i <= 97 and (ints[i] % 13 == 0 or ints[i] % 35 == 0):
            ints_div_by_either_nums.append(ints[i])
    if len(ints_div_by_either_nums) == 0:
        return 0
    else:
        return sum(ints_div_by_either_nums)