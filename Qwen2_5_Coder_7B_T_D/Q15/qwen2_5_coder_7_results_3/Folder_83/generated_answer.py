def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[90:201]) if i + 90 >= 90 and i + 90 <= 200 and (x % 2 != 0)))