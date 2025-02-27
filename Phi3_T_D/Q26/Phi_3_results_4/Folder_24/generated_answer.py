def sum_in_range(lst):
    total = sum(filter(lambda x: -91 <= x <= -41, lst))
    return total