def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(max(154, len(lst) - 1), min(798, len(lst) - 1) + 1):
        if lst[i] % 275 == 0 or lst[i] % 580 == 0:
            total += lst[i]
    return total