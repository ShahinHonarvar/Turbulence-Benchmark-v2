def sum_in_range(lst):
    return sum(filter(lambda x: -64 <= x <= 42, lst))