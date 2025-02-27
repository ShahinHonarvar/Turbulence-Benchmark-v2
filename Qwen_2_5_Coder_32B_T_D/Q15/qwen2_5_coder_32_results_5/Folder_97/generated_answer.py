def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[40:81] if x % 2 != 0)) if len(lst) > 80 else sum((x for x in lst[40:] if x % 2 != 0))