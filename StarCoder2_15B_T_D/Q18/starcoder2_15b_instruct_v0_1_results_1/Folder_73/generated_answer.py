def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 87:
        return 0
    divisible_ints = []
    for i in range(81, 87):
        if lst[i] % -33 == 0 or lst[i] % -62 == 0:
            divisible_ints.append(lst[i])
    return sum(divisible_ints)