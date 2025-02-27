def sum_ints_div_by_either_nums(lst):
    relevant_ints = lst[77:88]
    return sum((x for x in relevant_ints if x % 23 == 0 or x % 57 == 0))