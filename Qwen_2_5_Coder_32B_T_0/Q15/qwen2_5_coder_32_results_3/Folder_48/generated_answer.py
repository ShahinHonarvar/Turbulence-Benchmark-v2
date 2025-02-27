def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 533 <= i <= 605 and x % 2 != 0)) if len(lst) > 605 else 0