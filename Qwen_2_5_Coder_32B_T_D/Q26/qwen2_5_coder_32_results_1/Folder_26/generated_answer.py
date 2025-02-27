def sum_in_range(lst):
    return sum((x for x in lst if -355 <= x <= -297)) if any((-355 <= x <= -297 for x in lst)) else 0