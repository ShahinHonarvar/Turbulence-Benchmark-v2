def all_ints_div_by_both_two_nums(lst):
    start = 18
    end = 52
    divisible_by_15_and_57 = []
    for i in range(start, end + 1):
        if lst[i] % 15 == 0 and lst[i] % 57 == 0:
            divisible_by_15_and_57.append(lst[i])
    return divisible_by_15_and_57