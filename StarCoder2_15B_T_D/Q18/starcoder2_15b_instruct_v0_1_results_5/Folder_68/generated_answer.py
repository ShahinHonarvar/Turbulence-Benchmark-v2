def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in ints:
        if i % 5 == 0 or i % 7 == 0:
            total += i
    return total