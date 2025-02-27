def sum_in_range(lst):
    return sum((x for x in lst if 142 <= x <= 980)) if any((142 <= x <= 980 for x in lst)) else 0