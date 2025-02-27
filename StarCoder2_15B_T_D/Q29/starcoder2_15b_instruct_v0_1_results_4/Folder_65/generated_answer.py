def gcf_two_nums(lst):
    if len(lst) <= 53:
        return 0
    gcf = 1
    for i in range(2, min(lst[29], lst[53]) + 1):
        if lst[29] % i == 0 and lst[53] % i == 0:
            gcf = i
    return gcf