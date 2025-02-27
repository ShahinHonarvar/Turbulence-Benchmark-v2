def sum_in_range(lst):
    return sum((x for x in lst if 34 <= x <= 69)) if any((34 <= x <= 69 for x in lst)) else 0