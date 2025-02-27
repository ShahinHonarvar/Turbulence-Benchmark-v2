def sum_in_range(lst):
    return sum((x for x in lst if -798 <= x <= -379)) if any((-798 <= x <= -379 for x in lst)) else 0