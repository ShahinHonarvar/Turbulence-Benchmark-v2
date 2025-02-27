def sum_in_range(lst):
    return sum((x for x in lst if -816 <= x <= -166)) if any((-816 <= x <= -166 for x in lst)) else 0