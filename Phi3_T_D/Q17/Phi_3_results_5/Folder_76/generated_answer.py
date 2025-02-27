def all_ints_div_by_both_two_nums(records):
    return [x for x in records[250:630] if x % 850 == 0 and x % 587 == 0]